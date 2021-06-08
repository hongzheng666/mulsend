import time
import pyautogui
import subprocess
import pyperclip

# subprocess.call(["/usr/bin/open", "/Applications/企业微信.app"])
subprocess.Popen('C:\Program Files (x86)\WXWork\WXWork.exe')

mobileList = ['13173604500', '15967654063', '13173604500']
msg = '这是一条自动群发的消息反反复复'

def main():
  for mobile in mobileList:
    auto(mobile, msg)

def auto(mob, txt):
  pyperclip.copy(mob)

  time.sleep(0.5)
  # pyautogui.hotkey('command', 'f')
  pyautogui.hotkey('ctrl', 'f')

  time.sleep(0.5)
  # pyautogui.hotkey('command', 'v')
  pyautogui.hotkey('ctrl', 'v')

  time.sleep(0.5)
  pyautogui.press('enter')

  pyperclip.copy(mob + txt)

  time.sleep(0.5)
  # pyautogui.hotkey('command', 'v')
  pyautogui.hotkey('ctrl', 'v')

  time.sleep(0.5)
  pyautogui.press('enter')

main()
