from selenium import webdriver
import time

b = webdriver.Chrome('/usr/local/bin/chromedriver')

b.get('http://www.porters.vip/captcha/sliders.html')

time.sleep(2)
hover = b.find_element_by_css_selector('.hover')


def get_track(distance):  # distance为传入的总距离
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 / 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 1

    while current < distance:
        if current < mid:
            # 加速度为2
            a = 50
        else:
            # 加速度为-2
            a = -3
        v0 = v
        # 当前速度
        v = v0 + a * t
        # 移动距离
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move
        # 加入轨迹
        track.append(round(move))
    return track


def move_to_gap(slider, tracks):  # slider是要移动的滑块,tracks是要传入的移动轨迹

    print(tracks)

    action = webdriver.ActionChains(b)
    action.click_and_hold(slider).perform()
    for x in tracks:
        action.move_by_offset(xoffset=x, yoffset=0)
    time.sleep(0.5)
    action.release().perform()


if __name__ == '__main__':
    move_to_gap(hover, get_track(340))

