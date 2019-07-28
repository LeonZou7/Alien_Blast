import sys
import pygame
import time

from bullet import Bullet
from alien import Alien
from random import randint


def check_events(ab_settings, screen, stats, play_button, ship, aliens, bullets):
    # 事件监视
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ab_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ab_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ab_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    # 单击开始
    clicked = play_button.rect.collidepoint(mouse_x,mouse_y)

    if clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True
        ab_settings.init_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 清空全部
        aliens.empty()
        bullets.empty()

        # 还原初始状态
        ship.center_ship()
        create_fleet(ab_settings, screen, ship, aliens)


def check_keydown_events(event, ab_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ab_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def update_screen(ab_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button):
    # 显示按钮
    if not stats.game_active:
        play_button.draw_button()
    else:
        # 重绘窗口
        screen.fill(ab_settings.bg_color)

        # 绘制飞船
        ship.blitme()

        # 绘制Alien
        aliens.draw(screen)

        # 绘制子弹
        for bullet in bullets:
            bullet.draw_bullet()

        # 显示计分器
        scoreboard.show_score()

    # 窗口可见
    pygame.display.flip()


def get_alien_rows(ab_settigns, ship_height, alien_height):
    # 得到Alien的行数
    avaliable_space_y = (ab_settigns.screen_height - (alien_height * 3) - ship_height)
    number_rows = int(avaliable_space_y / (alien_height * 2))
    return number_rows


def get_num_of_alien_x(ab_settings, alien_width):
    # 得到一行Alien的数量
    avaliable_space_x = ab_settings.screen_width - (alien_width * 2)
    num_of_aliens_x = int(avaliable_space_x / (alien_width * 2))
    return num_of_aliens_x


def create_alien(ab_settings, screen, aliens, alien_number, alien_rows):
    # 创建Alien个体
    alien = Alien(ab_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + alien_width * alien_number * 2
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + alien.rect.height * alien_rows * 2
    aliens.add(alien)


def create_fleet(ab_settings, screen, ship, aliens):
    # 创建Alien群体
    alien = Alien(ab_settings, screen)
    alien_width = alien.rect.width
    num_of_aliens_x = get_num_of_alien_x(ab_settings, alien_width)
    rows = get_alien_rows(ab_settings, ship.rect.height, alien.rect.height)

    for row_number in range(rows):
        for alien_number in range(num_of_aliens_x):
            # 随机放置Alien
            set_alien = randint(1, 4) % 2
            if set_alien:
                create_alien(ab_settings, screen, aliens, alien_number, row_number)


def change_fleet_direction(ab_settings, aliens):
    for alien in aliens:
        alien.rect.y += ab_settings.alien_drop_speed
    ab_settings.alien_fleet_direction *= -1


def check_fleet_edge(ab_settings, aliens):
    # 监测Alien边缘碰撞
    for alien in aliens:
        if alien.check_edge():
            change_fleet_direction(ab_settings, aliens)
            break


def fire_bullets(ab_settings, screen, ship, bullets):
    # 发射子弹
    if len(bullets) <= ab_settings.bullet_max:
        new_bullet = Bullet(ab_settings, screen, ship)
        bullets.add(new_bullet)
        print(len(bullets))


def check_bullet_alien_collisions(ab_settings, screen, stats, scoreboard, ship, aliens, bullets):
    # 碰撞检测 两个True分别删除子弹和Alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # 增加得分
    if collisions:
        for aliens in collisions.values():
            # 分数 = 单只分数 * 数量
            stats.score += ab_settings.alien_points * len(aliens)
            scoreboard.prep_score()
        check_highest_score(stats, scoreboard)

    # 刷新Alien
    if len(aliens) == 0:
        ab_settings.increase_speed()
        create_fleet(ab_settings, screen, ship, aliens)


def check_alien_reach_bottom(ab_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            print("Alien breakthrough front!")
            ship_hit(ab_settings, stats, screen, ship, aliens, bullets)
            break


def check_highest_score(stats, scoreboard):
    # 检测新的最高分
    if stats.score > stats.highest_score:
        stats.highest_score = stats.score
        scoreboard.prep_highest_score()


def ship_hit(ab_settings, stats, screen, ship, aliens, bullets):
    # 飞船碰撞 重置游戏
    if stats.ship_life > 0:
        stats.ship_life -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(ab_settings, screen, ship, aliens)
        ship.center_ship()
        ab_settings.init_dynamic_settings()

        time.sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ab_settings, stats, screen, ship, aliens, bullets):
    # 移动Alien
    check_fleet_edge(ab_settings, aliens)
    aliens.update()

    # 飞船与Alien碰撞检测
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!")
        ship_hit(ab_settings, stats, screen, ship, aliens, bullets)

    # Alien到达底部监测
    check_alien_reach_bottom(ab_settings, stats, screen, ship, aliens, bullets)


def update_bullets(ab_settings, screen, stats, scoreboard, ship, aliens, bullets):
    # 子弹移动
    bullets.update()

    # 到达底部的子弹消除
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            print(len(bullets))

    check_bullet_alien_collisions(ab_settings, screen, stats, scoreboard, ship, aliens, bullets)
