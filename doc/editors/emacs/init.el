;; emacs to config

;;;;;;;;;;;;;;;;;;;; Basic setup ;;;;;;;;;;;;;;;;;;;;
;; Cancel the start interface
(setq inhibit-startup-message t)

;; Clean interface
(tool-bar-mode 0)
(menu-bar-mode 0)
(scroll-bar-mode 0)

;;;;;;;;;;;;;;;;;;;; end Basic setup ;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;; Personal settings ;;;;;;;;;;;;;;;;;;;;
;; No backup files are produced when saved
(setq make-backup-files nil)

;; Tab change space
(setq-default indent-tabs-mode nil)

;; when asking yes or no, answer with y-n
(fset 'yes-or-no-p 'y-or-n-p)

;; Automatic cursor for cursor
(mouse-avoidance-mode 'animate)

;; Extension matching
(show-paren-mode t)

;;Automatic completion symbol
(electric-pair-mode t)

;; Roll up and down
(setq scroll-conservatuvely 10000 scroll-margin 3 scroll-step 1)

;; Korea show here
;;(global-hl-line-mode t)

;; line number
(global-linum-mode t)
;;(setq linum-format "%d->")

;; time settings
(display-time-mode t)
(setq display-time-24hr-format t)
(setq display-time-day-and-date t)

;; show Column number
(column-number-mode t)

;; parenthesis matching
(show-paren-mode t)

;;set transparent effect
(global-set-key [(f12)] 'loop-alpha)
(setq alpha-list '((100 100) (95 75) (90 70) (85 65) (80 60) (75 55) (65 45) (55 35)))
(defun loop-alpha ()
  (interactive)
  (let ((h (car alpha-list)))  ;; head value will set to
    ((lambda (a ab)
       (set-frame-parameter (selected-frame) 'alpha (list a ab))
       (add-to-list 'default-frame-alist (cons 'alpha (list a ab)))
       ) (car h) (car (cdr h)))
    (setq alpha-list (cdr (append alpha-list (list h))))
    )
)

;;;;;;;;;;;;;;;;;;;; End personal settings ;;;;;;;;;;;;;;;;;;;;

