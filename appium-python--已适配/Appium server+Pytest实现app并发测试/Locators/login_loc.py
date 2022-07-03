# _*_ coding：utf-8 _*_

from selenium.webdriver.common.by import By

nen_close_inform = By.XPATH, '//*[@resource-id="com.android.systemui:id/notification_stack_scroller"]'



nen_username = By.XPATH, '//*[@resource-id="com.netease.newsreader.activity:id/arv"]'
nen_password = By.XPATH, '//*[@resource-id="com.netease.newsreader.activity:id/as9"]'
nen_pwd_hint = By.XPATH, '//*[@resource-id="com.netease.newsreader.activity:id/a3y"]'   # 密码框提示
nen_登录按钮 = By.XPATH, "//*[@text='开始使用']"
nen_协议 = By.XPATH, '//*[@text="同意"]'





nen_fenlei = By.CLASS_NAME, "android.widget.ImageView"