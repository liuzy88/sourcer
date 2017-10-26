
/** json_print_pretty pretty print the passed argument (type/data/length). */
int json_print_pretty(json_printer *printer, int type, const char *data, uint32_t length)
{
	return json_print_mode(printer, type, data, length, 1);
}

/** json_print_raw prints without eye candy the passed argument (type/data/length). */
int json_print_raw(json_printer *printer, int type, const char *data, uint32_t length)
{
	return json_print_mode(printer, type, data, length, 0);
}

/** json_print_args takes multiple types and pass them to the printer function */
int json_print_args(json_printer *printer,
                    int (*f)(json_printer *, int, const char *, uint32_t),
                    ...)
{
	va_list ap;
	char *data;
	uint32_t length;
	int type, ret;

	ret = 0;
	va_start(ap, f);
	while ((type = va_arg(ap, int)) != -1) {
		switch (type) {
		case JSON_ARRAY_BEGIN:
		case JSON_ARRAY_END:
		case JSON_OBJECT_BEGIN:
		case JSON_OBJECT_END:
		case JSON_NULL:
		case JSON_TRUE:
		case JSON_FALSE:
			ret = (*f)(printer, type, NULL, 0);
			break;
		case JSON_INT:
		case JSON_FLOAT:
		case JSON_KEY:
		case JSON_STRING:
			data = va_arg(ap, char *);
			length = va_arg(ap, uint32_t);
			if (length == -1)
				length = strlen(data);
			ret = (*f)(printer, type, data, length);
			break;
		}
		if (ret)
			break;
	}
	va_end(ap);
	return ret;
}
