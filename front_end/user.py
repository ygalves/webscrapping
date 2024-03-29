def login(userName: str, password: str) -> bool:
    if (userName is None):
        return False
    args = [userName, password, 0]
    #result_args = execute_sql_query("CheckUser", args)
    result_args = True
    return (result_args)