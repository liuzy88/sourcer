# 源代码统计（代码行/注释行/空行）工具 - 可配置

## 导入

```
from sourcer import *
```

### 分析代码打印分析过程（测试）

```python
analys_debug('exp/Test.java')
```

```text
文件 exp/Test.java
类型 Java
  2| 多行|  * Test file
  3| 多行|  */
  4| 代码| package com;
  5| 空行| 
  7| 多行|  * @author liuzy
  8| 多行|  *
  9| 多行|  */
 10| 代码| public class Test {
 11| 空行| 
 13| 多行| 	 * @param args
   ┌====>| 	 */ //sdfsdf System.out.println();
 14| 多行| 	 */ //sdfsdf System.out.println("Hello World!");
 15| 代码| 	public static void main(String[] args) {
 16| 单行| 		// TODO Auto-generated method stub
   ┌====>| 		System.out.println();
 17| 代码| 		System.out.println("\\/*Hello!");
 18| 空行| 
   ┌====>| 		System.out.println();/* asdf//sdf*/ System.out.println();
 19| 代码| 		System.out.println("World!");/* asdf//sdf*/ System.out.println("World!");
 21| 多行| 		 * nothing
 22| 代码| 		 */ method(1);
   ┌====>| 		System.out.println();
 23| 代码| 		System.out.println("Hello World!*/");
 24| 代码| 	}
 26| 多行| 	static void method(int i) {
   ┌====>| 		System.out.println(); */ static { System.out.println();
 27| 代码| 		System.out.println("sta t\"ic111	11"); */ static { System.out.println("sta tic\"222 	22\"22 !");
   ┌====>| 		System.out.println();
 28| 代码| 		System.out.println("test!");
 29| 代码| 	}
 31| 多行| 	static void method(int i) {
 32| 多行| 		System.out.println(i);
 33| 代码| 		*/ static {
   ┌====>| 		System.out.println();
 34| 代码| 		System.out.println("static");
 35| 代码| 	}
 36| 代码| 	static void method(int i) {
 37| 代码| 		System.out.println(i);
 38| 代码| 	}
 39| 代码| }
总行:  39
代码:  18 占比: 46.15%
注释:  12 占比: 30.77%
空行:   3 占比:  7.69%
```

```python
analys_debug('exp/test.c')
```

```text
文件 exp/test.c
类型 C/C++
  1| 空行| 
  2| 多行| /** json_print_pretty pretty print the passed argument (type/data/length). */
  3| 代码| int json_print_pretty(json_printer *printer, int type, const char *data, uint32_t length)
  4| 代码| {
  5| 代码| 	return json_print_mode(printer, type, data, length, 1);
  6| 代码| }
  7| 空行| 
  8| 多行| /** json_print_raw prints without eye candy the passed argument (type/data/length). */
  9| 代码| int json_print_raw(json_printer *printer, int type, const char *data, uint32_t length)
 10| 代码| {
 11| 代码| 	return json_print_mode(printer, type, data, length, 0);
 12| 代码| }
 13| 空行| 
 14| 多行| /** json_print_args takes multiple types and pass them to the printer function */
 15| 代码| int json_print_args(json_printer *printer,
 16| 代码|                     int (*f)(json_printer *, int, const char *, uint32_t),
 17| 代码|                     ...)
 18| 代码| {
 19| 代码| 	va_list ap;
 20| 代码| 	char *data;
 21| 代码| 	uint32_t length;
 22| 代码| 	int type, ret;
 23| 空行| 
 24| 代码| 	ret = 0;
 25| 代码| 	va_start(ap, f);
 26| 代码| 	while ((type = va_arg(ap, int)) != -1) {
 27| 代码| 		switch (type) {
 28| 代码| 		case JSON_ARRAY_BEGIN:
 29| 代码| 		case JSON_ARRAY_END:
 30| 代码| 		case JSON_OBJECT_BEGIN:
 31| 代码| 		case JSON_OBJECT_END:
 32| 代码| 		case JSON_NULL:
 33| 代码| 		case JSON_TRUE:
 34| 代码| 		case JSON_FALSE:
 35| 代码| 			ret = (*f)(printer, type, NULL, 0);
 36| 代码| 			break;
 37| 代码| 		case JSON_INT:
 38| 代码| 		case JSON_FLOAT:
 39| 代码| 		case JSON_KEY:
 40| 代码| 		case JSON_STRING:
 41| 代码| 			data = va_arg(ap, char *);
 42| 代码| 			length = va_arg(ap, uint32_t);
 43| 代码| 			if (length == -1)
 44| 代码| 				length = strlen(data);
 45| 代码| 			ret = (*f)(printer, type, data, length);
 46| 代码| 			break;
 47| 代码| 		}
 48| 代码| 		if (ret)
 49| 代码| 			break;
 50| 代码| 	}
 51| 代码| 	va_end(ap);
 52| 代码| 	return ret;
 53| 代码| }
总行:  53
代码:  46 占比: 86.79%
注释:   3 占比:  5.66%
空行:   4 占比:  7.55%
```

### 某tag的代码的详情（测试）

```
info_dir_tag('D:\\GitHub\\rabbitmq-server', 'rabbitmq_v3_6_12')
```

### 当前代码详情（测试）

```python
info_dir('D:\\GitHub\\kafka')
```

```text
已配置的语言: ['ASP.NET', 'C#', 'C/C++', 'DOS', 'Delphi', 'Erlang', 'GO', 'JS', 'Java', 'Lua', 'PHP', 'Pascal', 'Python', 'Ruby', 'Scala', 'Shell', 'Swift', 'XML', 'html', 'xsl']
已配置的扩展名: ['.asp', '.aspx', '.bat', '.c', '.cmd', '.cpp', '.cs', '.erl', '.go', '.go', '.h', '.hrl', '.htm', '.html', '.inc', '.java', '.js', '.jsp', '.lua', '.pas', '.php', '.py', '.rb', '.scala', '.sh', '.swift', '.xml', '.xsl']
当前目录: D:\GitHub\kafka
包含的语言: ['DOS', 'Java', 'Python', 'Scala', 'Shell', 'html']
包含的扩展名: {'.sh': 34, '.java': 23, '.scala': 274, '.py': 17, '.html': 6, '.bat': 8}
忽略的扩展名: {'.sbt': 6, '.txt': 1, '.json': 158, '*': 15, '.md': 2, '.jar': 7, '.properties': 61, '.out': 2, '.conf': 1}
文件总数/处理/忽略: 615/362/253
统计结果:
 Language  Files  Code Lines  Comment Lines  Blank Lines  Total Lines  Total Per
   Scala:    274       21292           6822         3991        32912     75.21%
  Python:     17        3104           1013          909         5026     11.49%
    Java:     23        2050            624          443         3189      7.29%
   Shell:     34        1279            737          371         2387      5.45%
     DOS:      8         199              0           31          230      0.53%
    html:      6          16              0            0           16      0.04%
   Totals    362       27940           9196         5745        43760
```

### 统计某tag的代码（生产）

```
scan_tag('D:\\GitHub\\rabbitmq-server', 'rabbitmq_v3_6_12')
```

### 统计所有tag（生产）

```python
scan_all_tag('D:\\GitHub\\libjson')
```

```text
v0.4 2009-12-31 {'files': 3, 'codes': 1039, 'lines': 1337, 'comments': 128, 'blanks': 154}
v0.5 2010-01-14 {'files': 3, 'codes': 1041, 'lines': 1339, 'comments': 128, 'blanks': 154}
v0.6 2010-02-23 {'files': 3, 'codes': 1152, 'lines': 1480, 'comments': 140, 'blanks': 170}
v0.7 2010-04-10 {'files': 3, 'codes': 1353, 'lines': 1710, 'comments': 141, 'blanks': 198}
v0.8 2010-09-04 {'files': 3, 'codes': 1353, 'lines': 1710, 'comments': 141, 'blanks': 198}
```