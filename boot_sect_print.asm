;
; A boot sector that just prints Hello using a BIOS routine
;

mov ah, 0x0e ; Scrolling tty BIOS routine

mov al, 'H'
int 0x10
mov al, 'e'
int 0x10
mov al, 'l'
int 0x10
mov al, 'l'
int 0x10
mov al, 'o'
int 0x10

jmp $ ; Jump to current address forever

times 510-($-$$) db 0 ; Fill out rest of boot sector with zeros

dw 0xaa55 ; Last two bytes form the "magic number" so the BIOS knows its a boot sector.
