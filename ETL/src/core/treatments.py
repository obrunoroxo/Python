import typing as T

from ..core.utils import logger
from ..core.exceptions import ImpossibleToContinueError


def test( f_value: T.Optional[T.Any] = None, s_value: T.Optional[T.Any] = None ) -> T.List[ T.Dict[ T.Any, T.Type ] ] :
    if f_value is not None and s_value is not None:
        return [ { f_value: s_value }, { "Value's type": [ { "FValue": type( f_value ), "SValue": type( s_value ) } ] } ]
    else:
        f_value = 'test'
        s_value = 14
        return [ { f_value: s_value }, { "Value's type": [ { "FValue": type( f_value ), "SValue": type( s_value ) } ] } ]


def __is_alphabetic( value: T.Any ) -> bool:
    boolean = str( value ).isalpha()
    return boolean


def treatment( f_value: T.Any, f_type: T.Type, s_value: T.Optional[ T.Any ] = None, s_type: T.Optional[ T.Type ] = None ) -> T.Union[ bool, T.Tuple[ bool, bool ] ] :
    if s_value is None and s_type is None:
        if isinstance( f_value, f_type ) == True and __is_alphabetic( f_value ) == True:
            logger().info(f" The value ({ f_value }) and the type ({ s_value }) is TRUE")
            return True
        else:
            logger().info(f" The value ({ f_value }) and the type ({ f_type }) is FALSE")
            return False

    elif s_value is not None and s_type is not None:
        if ( isinstance( f_value, f_type ) == True and __is_alphabetic( f_value ) == True ) and ( isinstance( s_value, s_type ) == True and __is_alphabetic( s_value ) == True):
            logger().info(f" The value ({ f_value }) and the type ({ f_type }) is TRUE")
            logger().info(f" The value ({ s_value }) and the type ({ s_type }) is TRUE")
            return True, True
        else:
            logger().info(f" The value ({ f_value }) and the type ({ f_type }) is FALSE")
            logger().info(f" The value ({ s_value }) and the type ({ s_type }) is FALSE")
            return False, False

    else:
        raise ImpossibleToContinueError



teste = test( f_value = "Am i a fucking sucker? And why is it true?", s_value = True )
print(teste)