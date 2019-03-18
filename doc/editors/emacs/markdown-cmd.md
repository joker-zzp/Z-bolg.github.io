# Emacs Markdown 配置和快捷键

## 安装配置

安装 pandoc

`sudo apt-get install pandoc`

安装 markdown-mode

在 **Emacs** 中安装插件

`M-x package-list-packages ENT markdown-mode`

在 **Emacs** 配置文件中加入markdown-mode 配置

``` emacs
(autoload 'markdown-mode "markdown-mode"
    "Major mode for editing Markdown files" t)
(add-to-list 'auto-mode-alist '("\\.text\\'" . markdown-mode))
(add-to-list 'auto-mode-alist '("\\.markdown\\'" . markdown-mode))
(add-to-list 'auto-mode-alist '("\\.md\\'" . markdown-mode))
```

## 快捷键

**超链接：C-c C-a**

**C-c C-c L** 以 `[text](url)` 插入一个行内的连接。