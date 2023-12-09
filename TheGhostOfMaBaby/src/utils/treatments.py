

import typing as T

from ..utils.logger import logger
from ..utils.exceptions import ImpossibleToContinueError



def __is_alphabetic( value: T.Any ) -> bool:
    boolean = str( value ).isalpha()
    return boolean


def treatment(
    f_value: T.Any,
    f_type: T.Type,
    s_value: T.Optional[ T.Any ] = None,
    s_type: T.Optional[ T.Type ] = None
) -> T.Union[ bool, T.Tuple[ bool, bool ] ] :

    def log_info(value, value_type, result):
        logger().info(f"The value ({value}) and the type ({value_type}) is {result}")



    if s_value is None and s_type is None:
        result = isinstance(f_value, f_type) and __is_alphabetic(f_value)
        log_info(f_value, f_type, result)
        return result

    elif s_value is not None and s_type is not None:
        result_f = isinstance(f_value, f_type) and __is_alphabetic(f_value)
        result_s = isinstance(s_value, s_type) and __is_alphabetic(s_value)
        log_info(f_value, f_type, result_f)
        log_info(s_value, s_type, result_s)
        return result_f, result_s

    else:
        raise ImpossibleToContinueError 




    # if s_value is None and s_type is None:
    #     if isinstance( f_value, f_type ) == True and __is_alphabetic( f_value ) == True:
    #         logger().info(f" The value ({ f_value }) and the type ({ s_value }) is TRUE")
    #         return True
    #     else:
    #         logger().info(f" The value ({ f_value }) and the type ({ f_type }) is FALSE")
    #         return False

    # elif s_value is not None and s_type is not None:
    #     if ( isinstance( f_value, f_type ) == True and __is_alphabetic( f_value ) == True ) and ( isinstance( s_value, s_type ) == True and __is_alphabetic( s_value ) == True ) :
    #         logger().info(f" The value ({ f_value }) and the type ({ f_type }) is TRUE")
    #         logger().info(f" The value ({ s_value }) and the type ({ s_type }) is TRUE")
    #         return True, True
    #     elif ( isinstance( f_value, f_type ) == False and __is_alphabetic( f_value ) == False ) and ( isinstance( s_value, s_type ) == False and __is_alphabetic( s_value ) == False ) :
    #         logger().info(f" The value ({ f_value }) and the type ({ f_type }) is FALSE")
    #         logger().info(f" The value ({ s_value }) and the type ({ s_type }) is FALSE")
    #         return False, False

    # else:
    #     raise ImpossibleToContinueError