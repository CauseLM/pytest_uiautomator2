# _*_ coding：utf-8 _*_

from selenium.webdriver.common.by import By

nen_sou = By.XPATH, '//*[@resource-id="com.netease.newsreader.activity:id/bmt"]/android.widget.RelativeLayout[1]' # 搜索
nen_search = By.XPATH, '//*[@resource-id="com.netease.newsreader.activity:id/bn7"]'             # 搜索框
nen_search_btn = By.XPATH, '//*[@resource-id="com.netease.newsreader.activity:id/bmu"]'         # 执行搜索按钮
nen_sort = By.XPATH, '//*[@resource-id="com.netease.newsreader.activity:id/bgy"]'              # 分类框
nen_sort_btn = By.XPATH, '//*[@resource-id="com.netease.newsreader.activity:id/a1v"]'           # 分类按钮
nen_hot = By.XPATH, '//*[@resource-id="com.netease.newsreader.activity:id/ae2"]'                # 热搜
nen_info = By.XPATH, '//*[@resource-id="com.netease.newsreader.activity:id/ae0"]'               # 私信

nen_duanzi = By.XPATH, "//*[@text='段子']"                               # 段子按钮
nen_keji = By.XPATH, "//*[@text='科技']"                                 # 科技按钮

nen_home = By.XPATH, '//*[@content-desc="首页标签 4之1"]'
nen_视频 = By.XPATH, '//*[@content-desc="视频标签 4之2"]'
nen_圈子 = By.XPATH, '//*[@content-desc="圈子标签 4之3"]'
nen_wo = By.XPATH, '//*[contains(@content-desc,"4之4")]'