
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result



from inspect import signature as _mutmut_signature

def x__mutmut_trampoline__mutmut_orig(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_1(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['XXMUTANT_UNDER_TESTXX']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_2(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ[None]
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_3(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = None
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_4(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test != 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_5(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'XXfailXX':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_6(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('XXFailed programmaticallyXX')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_7(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test != 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_8(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'XXstatsXX':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_9(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ - '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_10(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + 'XX.XX' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_11(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' - orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_12(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig( **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_13(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args,)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_14(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = None
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_15(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ - '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_16(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + 'XX.XX' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_17(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' - orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_18(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ - '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_19(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + 'XX__mutmut_XX'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_20(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = None
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_21(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if  mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_22(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(None):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_23(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig( **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_24(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args,)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_25(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = None
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_26(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('XX.XX')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_27(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[+1]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_28(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-2]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_29(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[None]
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_30(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = None
    result = mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_31(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[None](*args, **kwargs)
    return result

def x__mutmut_trampoline__mutmut_32(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name]( **kwargs)
    return result

def x__mutmut_trampoline__mutmut_33(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args,)
    return result

def x__mutmut_trampoline__mutmut_34(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = None
    return result

x__mutmut_trampoline__mutmut_mutants = {
'x__mutmut_trampoline__mutmut_1': x__mutmut_trampoline__mutmut_1, 
    'x__mutmut_trampoline__mutmut_2': x__mutmut_trampoline__mutmut_2, 
    'x__mutmut_trampoline__mutmut_3': x__mutmut_trampoline__mutmut_3, 
    'x__mutmut_trampoline__mutmut_4': x__mutmut_trampoline__mutmut_4, 
    'x__mutmut_trampoline__mutmut_5': x__mutmut_trampoline__mutmut_5, 
    'x__mutmut_trampoline__mutmut_6': x__mutmut_trampoline__mutmut_6, 
    'x__mutmut_trampoline__mutmut_7': x__mutmut_trampoline__mutmut_7, 
    'x__mutmut_trampoline__mutmut_8': x__mutmut_trampoline__mutmut_8, 
    'x__mutmut_trampoline__mutmut_9': x__mutmut_trampoline__mutmut_9, 
    'x__mutmut_trampoline__mutmut_10': x__mutmut_trampoline__mutmut_10, 
    'x__mutmut_trampoline__mutmut_11': x__mutmut_trampoline__mutmut_11, 
    'x__mutmut_trampoline__mutmut_12': x__mutmut_trampoline__mutmut_12, 
    'x__mutmut_trampoline__mutmut_13': x__mutmut_trampoline__mutmut_13, 
    'x__mutmut_trampoline__mutmut_14': x__mutmut_trampoline__mutmut_14, 
    'x__mutmut_trampoline__mutmut_15': x__mutmut_trampoline__mutmut_15, 
    'x__mutmut_trampoline__mutmut_16': x__mutmut_trampoline__mutmut_16, 
    'x__mutmut_trampoline__mutmut_17': x__mutmut_trampoline__mutmut_17, 
    'x__mutmut_trampoline__mutmut_18': x__mutmut_trampoline__mutmut_18, 
    'x__mutmut_trampoline__mutmut_19': x__mutmut_trampoline__mutmut_19, 
    'x__mutmut_trampoline__mutmut_20': x__mutmut_trampoline__mutmut_20, 
    'x__mutmut_trampoline__mutmut_21': x__mutmut_trampoline__mutmut_21, 
    'x__mutmut_trampoline__mutmut_22': x__mutmut_trampoline__mutmut_22, 
    'x__mutmut_trampoline__mutmut_23': x__mutmut_trampoline__mutmut_23, 
    'x__mutmut_trampoline__mutmut_24': x__mutmut_trampoline__mutmut_24, 
    'x__mutmut_trampoline__mutmut_25': x__mutmut_trampoline__mutmut_25, 
    'x__mutmut_trampoline__mutmut_26': x__mutmut_trampoline__mutmut_26, 
    'x__mutmut_trampoline__mutmut_27': x__mutmut_trampoline__mutmut_27, 
    'x__mutmut_trampoline__mutmut_28': x__mutmut_trampoline__mutmut_28, 
    'x__mutmut_trampoline__mutmut_29': x__mutmut_trampoline__mutmut_29, 
    'x__mutmut_trampoline__mutmut_30': x__mutmut_trampoline__mutmut_30, 
    'x__mutmut_trampoline__mutmut_31': x__mutmut_trampoline__mutmut_31, 
    'x__mutmut_trampoline__mutmut_32': x__mutmut_trampoline__mutmut_32, 
    'x__mutmut_trampoline__mutmut_33': x__mutmut_trampoline__mutmut_33, 
    'x__mutmut_trampoline__mutmut_34': x__mutmut_trampoline__mutmut_34
}

def _mutmut_trampoline(*args, **kwargs):
    result = _mutmut_trampoline(x__mutmut_trampoline__mutmut_orig, x__mutmut_trampoline__mutmut_mutants, *args, **kwargs)
    return result 

_mutmut_trampoline.__signature__ = _mutmut_signature(x__mutmut_trampoline__mutmut_orig)
x__mutmut_trampoline__mutmut_orig.__name__ = 'x__mutmut_trampoline'




from inspect import signature as _mutmut_signature

def x__mutmut_yield_from_trampoline__mutmut_orig(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_1(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['XXMUTANT_UNDER_TESTXX']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_2(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ[None]
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_3(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = None
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_4(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test != 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_5(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'XXfailXX':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_6(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('XXFailed programmaticallyXX')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_7(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test != 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_8(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'XXstatsXX':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_9(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ - '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_10(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + 'XX.XX' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_11(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' - orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_12(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig( **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_13(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args,)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_14(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = None
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_15(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ - '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_16(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + 'XX.XX' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_17(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' - orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_18(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ - '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_19(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + 'XX__mutmut_XX'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_20(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = None
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_21(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if  mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_22(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(None):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_23(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig( **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_24(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args,)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_25(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = None
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_26(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('XX.XX')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_27(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[+1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_28(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-2]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_29(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[None]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_30(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = None
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_31(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[None](*args, **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_32(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name]( **kwargs)
    return result

def x__mutmut_yield_from_trampoline__mutmut_33(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args,)
    return result

def x__mutmut_yield_from_trampoline__mutmut_34(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = None
    return result

x__mutmut_yield_from_trampoline__mutmut_mutants = {
'x__mutmut_yield_from_trampoline__mutmut_1': x__mutmut_yield_from_trampoline__mutmut_1, 
    'x__mutmut_yield_from_trampoline__mutmut_2': x__mutmut_yield_from_trampoline__mutmut_2, 
    'x__mutmut_yield_from_trampoline__mutmut_3': x__mutmut_yield_from_trampoline__mutmut_3, 
    'x__mutmut_yield_from_trampoline__mutmut_4': x__mutmut_yield_from_trampoline__mutmut_4, 
    'x__mutmut_yield_from_trampoline__mutmut_5': x__mutmut_yield_from_trampoline__mutmut_5, 
    'x__mutmut_yield_from_trampoline__mutmut_6': x__mutmut_yield_from_trampoline__mutmut_6, 
    'x__mutmut_yield_from_trampoline__mutmut_7': x__mutmut_yield_from_trampoline__mutmut_7, 
    'x__mutmut_yield_from_trampoline__mutmut_8': x__mutmut_yield_from_trampoline__mutmut_8, 
    'x__mutmut_yield_from_trampoline__mutmut_9': x__mutmut_yield_from_trampoline__mutmut_9, 
    'x__mutmut_yield_from_trampoline__mutmut_10': x__mutmut_yield_from_trampoline__mutmut_10, 
    'x__mutmut_yield_from_trampoline__mutmut_11': x__mutmut_yield_from_trampoline__mutmut_11, 
    'x__mutmut_yield_from_trampoline__mutmut_12': x__mutmut_yield_from_trampoline__mutmut_12, 
    'x__mutmut_yield_from_trampoline__mutmut_13': x__mutmut_yield_from_trampoline__mutmut_13, 
    'x__mutmut_yield_from_trampoline__mutmut_14': x__mutmut_yield_from_trampoline__mutmut_14, 
    'x__mutmut_yield_from_trampoline__mutmut_15': x__mutmut_yield_from_trampoline__mutmut_15, 
    'x__mutmut_yield_from_trampoline__mutmut_16': x__mutmut_yield_from_trampoline__mutmut_16, 
    'x__mutmut_yield_from_trampoline__mutmut_17': x__mutmut_yield_from_trampoline__mutmut_17, 
    'x__mutmut_yield_from_trampoline__mutmut_18': x__mutmut_yield_from_trampoline__mutmut_18, 
    'x__mutmut_yield_from_trampoline__mutmut_19': x__mutmut_yield_from_trampoline__mutmut_19, 
    'x__mutmut_yield_from_trampoline__mutmut_20': x__mutmut_yield_from_trampoline__mutmut_20, 
    'x__mutmut_yield_from_trampoline__mutmut_21': x__mutmut_yield_from_trampoline__mutmut_21, 
    'x__mutmut_yield_from_trampoline__mutmut_22': x__mutmut_yield_from_trampoline__mutmut_22, 
    'x__mutmut_yield_from_trampoline__mutmut_23': x__mutmut_yield_from_trampoline__mutmut_23, 
    'x__mutmut_yield_from_trampoline__mutmut_24': x__mutmut_yield_from_trampoline__mutmut_24, 
    'x__mutmut_yield_from_trampoline__mutmut_25': x__mutmut_yield_from_trampoline__mutmut_25, 
    'x__mutmut_yield_from_trampoline__mutmut_26': x__mutmut_yield_from_trampoline__mutmut_26, 
    'x__mutmut_yield_from_trampoline__mutmut_27': x__mutmut_yield_from_trampoline__mutmut_27, 
    'x__mutmut_yield_from_trampoline__mutmut_28': x__mutmut_yield_from_trampoline__mutmut_28, 
    'x__mutmut_yield_from_trampoline__mutmut_29': x__mutmut_yield_from_trampoline__mutmut_29, 
    'x__mutmut_yield_from_trampoline__mutmut_30': x__mutmut_yield_from_trampoline__mutmut_30, 
    'x__mutmut_yield_from_trampoline__mutmut_31': x__mutmut_yield_from_trampoline__mutmut_31, 
    'x__mutmut_yield_from_trampoline__mutmut_32': x__mutmut_yield_from_trampoline__mutmut_32, 
    'x__mutmut_yield_from_trampoline__mutmut_33': x__mutmut_yield_from_trampoline__mutmut_33, 
    'x__mutmut_yield_from_trampoline__mutmut_34': x__mutmut_yield_from_trampoline__mutmut_34
}

def _mutmut_yield_from_trampoline(*args, **kwargs):
    result = yield from _mutmut_yield_from_trampoline(x__mutmut_yield_from_trampoline__mutmut_orig, x__mutmut_yield_from_trampoline__mutmut_mutants, *args, **kwargs)
    return result 

_mutmut_yield_from_trampoline.__signature__ = _mutmut_signature(x__mutmut_yield_from_trampoline__mutmut_orig)
x__mutmut_yield_from_trampoline__mutmut_orig.__name__ = 'x__mutmut_yield_from_trampoline'




from src.is_prime import is_prime

def x_x_test_is_prime_basics__mutmut_orig__mutmut_orig():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_orig__mutmut_1():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_orig__mutmut_2():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_orig__mutmut_3():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_orig__mutmut_4():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_orig__mutmut_5():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_orig__mutmut_6():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_orig__mutmut_7():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_orig__mutmut_8():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_orig__mutmut_9():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

x_x_test_is_prime_basics__mutmut_orig__mutmut_mutants = {
'x_x_test_is_prime_basics__mutmut_orig__mutmut_1': x_x_test_is_prime_basics__mutmut_orig__mutmut_1, 
    'x_x_test_is_prime_basics__mutmut_orig__mutmut_2': x_x_test_is_prime_basics__mutmut_orig__mutmut_2, 
    'x_x_test_is_prime_basics__mutmut_orig__mutmut_3': x_x_test_is_prime_basics__mutmut_orig__mutmut_3, 
    'x_x_test_is_prime_basics__mutmut_orig__mutmut_4': x_x_test_is_prime_basics__mutmut_orig__mutmut_4, 
    'x_x_test_is_prime_basics__mutmut_orig__mutmut_5': x_x_test_is_prime_basics__mutmut_orig__mutmut_5, 
    'x_x_test_is_prime_basics__mutmut_orig__mutmut_6': x_x_test_is_prime_basics__mutmut_orig__mutmut_6, 
    'x_x_test_is_prime_basics__mutmut_orig__mutmut_7': x_x_test_is_prime_basics__mutmut_orig__mutmut_7, 
    'x_x_test_is_prime_basics__mutmut_orig__mutmut_8': x_x_test_is_prime_basics__mutmut_orig__mutmut_8, 
    'x_x_test_is_prime_basics__mutmut_orig__mutmut_9': x_x_test_is_prime_basics__mutmut_orig__mutmut_9
}

def x_test_is_prime_basics__mutmut_orig(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_basics__mutmut_orig__mutmut_orig, x_x_test_is_prime_basics__mutmut_orig__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_basics__mutmut_orig.__signature__ = _mutmut_signature(x_x_test_is_prime_basics__mutmut_orig__mutmut_orig)
x_x_test_is_prime_basics__mutmut_orig__mutmut_orig.__name__ = 'x_x_test_is_prime_basics__mutmut_orig'



def x_x_test_is_prime_basics__mutmut_1__mutmut_orig():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_1__mutmut_1():
  # casos basicos
  assert  is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_1__mutmut_2():
  # casos basicos
  assert  is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_1__mutmut_3():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_1__mutmut_4():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_1__mutmut_5():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_1__mutmut_6():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_1__mutmut_7():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_1__mutmut_8():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

x_x_test_is_prime_basics__mutmut_1__mutmut_mutants = {
'x_x_test_is_prime_basics__mutmut_1__mutmut_1': x_x_test_is_prime_basics__mutmut_1__mutmut_1, 
    'x_x_test_is_prime_basics__mutmut_1__mutmut_2': x_x_test_is_prime_basics__mutmut_1__mutmut_2, 
    'x_x_test_is_prime_basics__mutmut_1__mutmut_3': x_x_test_is_prime_basics__mutmut_1__mutmut_3, 
    'x_x_test_is_prime_basics__mutmut_1__mutmut_4': x_x_test_is_prime_basics__mutmut_1__mutmut_4, 
    'x_x_test_is_prime_basics__mutmut_1__mutmut_5': x_x_test_is_prime_basics__mutmut_1__mutmut_5, 
    'x_x_test_is_prime_basics__mutmut_1__mutmut_6': x_x_test_is_prime_basics__mutmut_1__mutmut_6, 
    'x_x_test_is_prime_basics__mutmut_1__mutmut_7': x_x_test_is_prime_basics__mutmut_1__mutmut_7, 
    'x_x_test_is_prime_basics__mutmut_1__mutmut_8': x_x_test_is_prime_basics__mutmut_1__mutmut_8
}

def x_test_is_prime_basics__mutmut_1(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_basics__mutmut_1__mutmut_orig, x_x_test_is_prime_basics__mutmut_1__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_basics__mutmut_1.__signature__ = _mutmut_signature(x_x_test_is_prime_basics__mutmut_1__mutmut_orig)
x_x_test_is_prime_basics__mutmut_1__mutmut_orig.__name__ = 'x_x_test_is_prime_basics__mutmut_1'



def x_x_test_is_prime_basics__mutmut_2__mutmut_orig():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_2__mutmut_1():
  # casos basicos
  assert  is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_2__mutmut_2():
  # casos basicos
  assert not is_prime(2)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_2__mutmut_3():
  # casos basicos
  assert not is_prime(1)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_2__mutmut_4():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_2__mutmut_5():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_2__mutmut_6():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_2__mutmut_7():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_2__mutmut_8():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_2__mutmut_9():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

x_x_test_is_prime_basics__mutmut_2__mutmut_mutants = {
'x_x_test_is_prime_basics__mutmut_2__mutmut_1': x_x_test_is_prime_basics__mutmut_2__mutmut_1, 
    'x_x_test_is_prime_basics__mutmut_2__mutmut_2': x_x_test_is_prime_basics__mutmut_2__mutmut_2, 
    'x_x_test_is_prime_basics__mutmut_2__mutmut_3': x_x_test_is_prime_basics__mutmut_2__mutmut_3, 
    'x_x_test_is_prime_basics__mutmut_2__mutmut_4': x_x_test_is_prime_basics__mutmut_2__mutmut_4, 
    'x_x_test_is_prime_basics__mutmut_2__mutmut_5': x_x_test_is_prime_basics__mutmut_2__mutmut_5, 
    'x_x_test_is_prime_basics__mutmut_2__mutmut_6': x_x_test_is_prime_basics__mutmut_2__mutmut_6, 
    'x_x_test_is_prime_basics__mutmut_2__mutmut_7': x_x_test_is_prime_basics__mutmut_2__mutmut_7, 
    'x_x_test_is_prime_basics__mutmut_2__mutmut_8': x_x_test_is_prime_basics__mutmut_2__mutmut_8, 
    'x_x_test_is_prime_basics__mutmut_2__mutmut_9': x_x_test_is_prime_basics__mutmut_2__mutmut_9
}

def x_test_is_prime_basics__mutmut_2(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_basics__mutmut_2__mutmut_orig, x_x_test_is_prime_basics__mutmut_2__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_basics__mutmut_2.__signature__ = _mutmut_signature(x_x_test_is_prime_basics__mutmut_2__mutmut_orig)
x_x_test_is_prime_basics__mutmut_2__mutmut_orig.__name__ = 'x_x_test_is_prime_basics__mutmut_2'



def x_x_test_is_prime_basics__mutmut_3__mutmut_orig():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_3__mutmut_1():
  # casos basicos
  assert  is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_3__mutmut_2():
  # casos basicos
  assert not is_prime(1)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_3__mutmut_3():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_3__mutmut_4():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_3__mutmut_5():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_3__mutmut_6():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_3__mutmut_7():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_3__mutmut_8():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

x_x_test_is_prime_basics__mutmut_3__mutmut_mutants = {
'x_x_test_is_prime_basics__mutmut_3__mutmut_1': x_x_test_is_prime_basics__mutmut_3__mutmut_1, 
    'x_x_test_is_prime_basics__mutmut_3__mutmut_2': x_x_test_is_prime_basics__mutmut_3__mutmut_2, 
    'x_x_test_is_prime_basics__mutmut_3__mutmut_3': x_x_test_is_prime_basics__mutmut_3__mutmut_3, 
    'x_x_test_is_prime_basics__mutmut_3__mutmut_4': x_x_test_is_prime_basics__mutmut_3__mutmut_4, 
    'x_x_test_is_prime_basics__mutmut_3__mutmut_5': x_x_test_is_prime_basics__mutmut_3__mutmut_5, 
    'x_x_test_is_prime_basics__mutmut_3__mutmut_6': x_x_test_is_prime_basics__mutmut_3__mutmut_6, 
    'x_x_test_is_prime_basics__mutmut_3__mutmut_7': x_x_test_is_prime_basics__mutmut_3__mutmut_7, 
    'x_x_test_is_prime_basics__mutmut_3__mutmut_8': x_x_test_is_prime_basics__mutmut_3__mutmut_8
}

def x_test_is_prime_basics__mutmut_3(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_basics__mutmut_3__mutmut_orig, x_x_test_is_prime_basics__mutmut_3__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_basics__mutmut_3.__signature__ = _mutmut_signature(x_x_test_is_prime_basics__mutmut_3__mutmut_orig)
x_x_test_is_prime_basics__mutmut_3__mutmut_orig.__name__ = 'x_x_test_is_prime_basics__mutmut_3'



def x_x_test_is_prime_basics__mutmut_4__mutmut_orig():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_4__mutmut_1():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_4__mutmut_2():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_4__mutmut_3():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_4__mutmut_4():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(3)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_4__mutmut_5():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_4__mutmut_6():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_4__mutmut_7():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_4__mutmut_8():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_4__mutmut_9():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

x_x_test_is_prime_basics__mutmut_4__mutmut_mutants = {
'x_x_test_is_prime_basics__mutmut_4__mutmut_1': x_x_test_is_prime_basics__mutmut_4__mutmut_1, 
    'x_x_test_is_prime_basics__mutmut_4__mutmut_2': x_x_test_is_prime_basics__mutmut_4__mutmut_2, 
    'x_x_test_is_prime_basics__mutmut_4__mutmut_3': x_x_test_is_prime_basics__mutmut_4__mutmut_3, 
    'x_x_test_is_prime_basics__mutmut_4__mutmut_4': x_x_test_is_prime_basics__mutmut_4__mutmut_4, 
    'x_x_test_is_prime_basics__mutmut_4__mutmut_5': x_x_test_is_prime_basics__mutmut_4__mutmut_5, 
    'x_x_test_is_prime_basics__mutmut_4__mutmut_6': x_x_test_is_prime_basics__mutmut_4__mutmut_6, 
    'x_x_test_is_prime_basics__mutmut_4__mutmut_7': x_x_test_is_prime_basics__mutmut_4__mutmut_7, 
    'x_x_test_is_prime_basics__mutmut_4__mutmut_8': x_x_test_is_prime_basics__mutmut_4__mutmut_8, 
    'x_x_test_is_prime_basics__mutmut_4__mutmut_9': x_x_test_is_prime_basics__mutmut_4__mutmut_9
}

def x_test_is_prime_basics__mutmut_4(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_basics__mutmut_4__mutmut_orig, x_x_test_is_prime_basics__mutmut_4__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_basics__mutmut_4.__signature__ = _mutmut_signature(x_x_test_is_prime_basics__mutmut_4__mutmut_orig)
x_x_test_is_prime_basics__mutmut_4__mutmut_orig.__name__ = 'x_x_test_is_prime_basics__mutmut_4'



def x_x_test_is_prime_basics__mutmut_5__mutmut_orig():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_5__mutmut_1():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_5__mutmut_2():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_5__mutmut_3():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_5__mutmut_4():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_5__mutmut_5():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(4)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_5__mutmut_6():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_5__mutmut_7():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_5__mutmut_8():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_5__mutmut_9():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

x_x_test_is_prime_basics__mutmut_5__mutmut_mutants = {
'x_x_test_is_prime_basics__mutmut_5__mutmut_1': x_x_test_is_prime_basics__mutmut_5__mutmut_1, 
    'x_x_test_is_prime_basics__mutmut_5__mutmut_2': x_x_test_is_prime_basics__mutmut_5__mutmut_2, 
    'x_x_test_is_prime_basics__mutmut_5__mutmut_3': x_x_test_is_prime_basics__mutmut_5__mutmut_3, 
    'x_x_test_is_prime_basics__mutmut_5__mutmut_4': x_x_test_is_prime_basics__mutmut_5__mutmut_4, 
    'x_x_test_is_prime_basics__mutmut_5__mutmut_5': x_x_test_is_prime_basics__mutmut_5__mutmut_5, 
    'x_x_test_is_prime_basics__mutmut_5__mutmut_6': x_x_test_is_prime_basics__mutmut_5__mutmut_6, 
    'x_x_test_is_prime_basics__mutmut_5__mutmut_7': x_x_test_is_prime_basics__mutmut_5__mutmut_7, 
    'x_x_test_is_prime_basics__mutmut_5__mutmut_8': x_x_test_is_prime_basics__mutmut_5__mutmut_8, 
    'x_x_test_is_prime_basics__mutmut_5__mutmut_9': x_x_test_is_prime_basics__mutmut_5__mutmut_9
}

def x_test_is_prime_basics__mutmut_5(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_basics__mutmut_5__mutmut_orig, x_x_test_is_prime_basics__mutmut_5__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_basics__mutmut_5.__signature__ = _mutmut_signature(x_x_test_is_prime_basics__mutmut_5__mutmut_orig)
x_x_test_is_prime_basics__mutmut_5__mutmut_orig.__name__ = 'x_x_test_is_prime_basics__mutmut_5'



def x_x_test_is_prime_basics__mutmut_6__mutmut_orig():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_6__mutmut_1():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_6__mutmut_2():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_6__mutmut_3():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_6__mutmut_4():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_6__mutmut_5():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_6__mutmut_6():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(5)
  assert not is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_6__mutmut_7():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_6__mutmut_8():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_6__mutmut_9():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(6)

x_x_test_is_prime_basics__mutmut_6__mutmut_mutants = {
'x_x_test_is_prime_basics__mutmut_6__mutmut_1': x_x_test_is_prime_basics__mutmut_6__mutmut_1, 
    'x_x_test_is_prime_basics__mutmut_6__mutmut_2': x_x_test_is_prime_basics__mutmut_6__mutmut_2, 
    'x_x_test_is_prime_basics__mutmut_6__mutmut_3': x_x_test_is_prime_basics__mutmut_6__mutmut_3, 
    'x_x_test_is_prime_basics__mutmut_6__mutmut_4': x_x_test_is_prime_basics__mutmut_6__mutmut_4, 
    'x_x_test_is_prime_basics__mutmut_6__mutmut_5': x_x_test_is_prime_basics__mutmut_6__mutmut_5, 
    'x_x_test_is_prime_basics__mutmut_6__mutmut_6': x_x_test_is_prime_basics__mutmut_6__mutmut_6, 
    'x_x_test_is_prime_basics__mutmut_6__mutmut_7': x_x_test_is_prime_basics__mutmut_6__mutmut_7, 
    'x_x_test_is_prime_basics__mutmut_6__mutmut_8': x_x_test_is_prime_basics__mutmut_6__mutmut_8, 
    'x_x_test_is_prime_basics__mutmut_6__mutmut_9': x_x_test_is_prime_basics__mutmut_6__mutmut_9
}

def x_test_is_prime_basics__mutmut_6(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_basics__mutmut_6__mutmut_orig, x_x_test_is_prime_basics__mutmut_6__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_basics__mutmut_6.__signature__ = _mutmut_signature(x_x_test_is_prime_basics__mutmut_6__mutmut_orig)
x_x_test_is_prime_basics__mutmut_6__mutmut_orig.__name__ = 'x_x_test_is_prime_basics__mutmut_6'



def x_x_test_is_prime_basics__mutmut_7__mutmut_orig():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_7__mutmut_1():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_7__mutmut_2():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_7__mutmut_3():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_7__mutmut_4():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_7__mutmut_5():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_7__mutmut_6():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert  is_prime(4)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_7__mutmut_7():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_7__mutmut_8():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(6)

x_x_test_is_prime_basics__mutmut_7__mutmut_mutants = {
'x_x_test_is_prime_basics__mutmut_7__mutmut_1': x_x_test_is_prime_basics__mutmut_7__mutmut_1, 
    'x_x_test_is_prime_basics__mutmut_7__mutmut_2': x_x_test_is_prime_basics__mutmut_7__mutmut_2, 
    'x_x_test_is_prime_basics__mutmut_7__mutmut_3': x_x_test_is_prime_basics__mutmut_7__mutmut_3, 
    'x_x_test_is_prime_basics__mutmut_7__mutmut_4': x_x_test_is_prime_basics__mutmut_7__mutmut_4, 
    'x_x_test_is_prime_basics__mutmut_7__mutmut_5': x_x_test_is_prime_basics__mutmut_7__mutmut_5, 
    'x_x_test_is_prime_basics__mutmut_7__mutmut_6': x_x_test_is_prime_basics__mutmut_7__mutmut_6, 
    'x_x_test_is_prime_basics__mutmut_7__mutmut_7': x_x_test_is_prime_basics__mutmut_7__mutmut_7, 
    'x_x_test_is_prime_basics__mutmut_7__mutmut_8': x_x_test_is_prime_basics__mutmut_7__mutmut_8
}

def x_test_is_prime_basics__mutmut_7(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_basics__mutmut_7__mutmut_orig, x_x_test_is_prime_basics__mutmut_7__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_basics__mutmut_7.__signature__ = _mutmut_signature(x_x_test_is_prime_basics__mutmut_7__mutmut_orig)
x_x_test_is_prime_basics__mutmut_7__mutmut_orig.__name__ = 'x_x_test_is_prime_basics__mutmut_7'



def x_x_test_is_prime_basics__mutmut_8__mutmut_orig():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_8__mutmut_1():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_8__mutmut_2():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_8__mutmut_3():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_8__mutmut_4():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_8__mutmut_5():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_8__mutmut_6():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_8__mutmut_7():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(5)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_8__mutmut_8():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(6)
  assert is_prime(5)

def x_x_test_is_prime_basics__mutmut_8__mutmut_9():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(6)

x_x_test_is_prime_basics__mutmut_8__mutmut_mutants = {
'x_x_test_is_prime_basics__mutmut_8__mutmut_1': x_x_test_is_prime_basics__mutmut_8__mutmut_1, 
    'x_x_test_is_prime_basics__mutmut_8__mutmut_2': x_x_test_is_prime_basics__mutmut_8__mutmut_2, 
    'x_x_test_is_prime_basics__mutmut_8__mutmut_3': x_x_test_is_prime_basics__mutmut_8__mutmut_3, 
    'x_x_test_is_prime_basics__mutmut_8__mutmut_4': x_x_test_is_prime_basics__mutmut_8__mutmut_4, 
    'x_x_test_is_prime_basics__mutmut_8__mutmut_5': x_x_test_is_prime_basics__mutmut_8__mutmut_5, 
    'x_x_test_is_prime_basics__mutmut_8__mutmut_6': x_x_test_is_prime_basics__mutmut_8__mutmut_6, 
    'x_x_test_is_prime_basics__mutmut_8__mutmut_7': x_x_test_is_prime_basics__mutmut_8__mutmut_7, 
    'x_x_test_is_prime_basics__mutmut_8__mutmut_8': x_x_test_is_prime_basics__mutmut_8__mutmut_8, 
    'x_x_test_is_prime_basics__mutmut_8__mutmut_9': x_x_test_is_prime_basics__mutmut_8__mutmut_9
}

def x_test_is_prime_basics__mutmut_8(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_basics__mutmut_8__mutmut_orig, x_x_test_is_prime_basics__mutmut_8__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_basics__mutmut_8.__signature__ = _mutmut_signature(x_x_test_is_prime_basics__mutmut_8__mutmut_orig)
x_x_test_is_prime_basics__mutmut_8__mutmut_orig.__name__ = 'x_x_test_is_prime_basics__mutmut_8'



def x_x_test_is_prime_basics__mutmut_9__mutmut_orig():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

def x_x_test_is_prime_basics__mutmut_9__mutmut_1():
  # casos basicos
  assert  is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

def x_x_test_is_prime_basics__mutmut_9__mutmut_2():
  # casos basicos
  assert not is_prime(1)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

def x_x_test_is_prime_basics__mutmut_9__mutmut_3():
  # casos basicos
  assert not is_prime(0)
  assert  is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

def x_x_test_is_prime_basics__mutmut_9__mutmut_4():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(2)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

def x_x_test_is_prime_basics__mutmut_9__mutmut_5():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(3)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(6)

def x_x_test_is_prime_basics__mutmut_9__mutmut_6():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(4)
  assert not is_prime(4)
  assert is_prime(6)

def x_x_test_is_prime_basics__mutmut_9__mutmut_7():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert  is_prime(4)
  assert is_prime(6)

def x_x_test_is_prime_basics__mutmut_9__mutmut_8():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(5)
  assert is_prime(6)

def x_x_test_is_prime_basics__mutmut_9__mutmut_9():
  # casos basicos
  assert not is_prime(0)
  assert not is_prime(1)
  assert is_prime(2)
  assert is_prime(3)
  assert not is_prime(4)
  assert is_prime(7)

x_x_test_is_prime_basics__mutmut_9__mutmut_mutants = {
'x_x_test_is_prime_basics__mutmut_9__mutmut_1': x_x_test_is_prime_basics__mutmut_9__mutmut_1, 
    'x_x_test_is_prime_basics__mutmut_9__mutmut_2': x_x_test_is_prime_basics__mutmut_9__mutmut_2, 
    'x_x_test_is_prime_basics__mutmut_9__mutmut_3': x_x_test_is_prime_basics__mutmut_9__mutmut_3, 
    'x_x_test_is_prime_basics__mutmut_9__mutmut_4': x_x_test_is_prime_basics__mutmut_9__mutmut_4, 
    'x_x_test_is_prime_basics__mutmut_9__mutmut_5': x_x_test_is_prime_basics__mutmut_9__mutmut_5, 
    'x_x_test_is_prime_basics__mutmut_9__mutmut_6': x_x_test_is_prime_basics__mutmut_9__mutmut_6, 
    'x_x_test_is_prime_basics__mutmut_9__mutmut_7': x_x_test_is_prime_basics__mutmut_9__mutmut_7, 
    'x_x_test_is_prime_basics__mutmut_9__mutmut_8': x_x_test_is_prime_basics__mutmut_9__mutmut_8, 
    'x_x_test_is_prime_basics__mutmut_9__mutmut_9': x_x_test_is_prime_basics__mutmut_9__mutmut_9
}

def x_test_is_prime_basics__mutmut_9(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_basics__mutmut_9__mutmut_orig, x_x_test_is_prime_basics__mutmut_9__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_basics__mutmut_9.__signature__ = _mutmut_signature(x_x_test_is_prime_basics__mutmut_9__mutmut_orig)
x_x_test_is_prime_basics__mutmut_9__mutmut_orig.__name__ = 'x_x_test_is_prime_basics__mutmut_9'



x_test_is_prime_basics__mutmut_mutants = {
'x_test_is_prime_basics__mutmut_1': x_test_is_prime_basics__mutmut_1, 
    'x_test_is_prime_basics__mutmut_2': x_test_is_prime_basics__mutmut_2, 
    'x_test_is_prime_basics__mutmut_3': x_test_is_prime_basics__mutmut_3, 
    'x_test_is_prime_basics__mutmut_4': x_test_is_prime_basics__mutmut_4, 
    'x_test_is_prime_basics__mutmut_5': x_test_is_prime_basics__mutmut_5, 
    'x_test_is_prime_basics__mutmut_6': x_test_is_prime_basics__mutmut_6, 
    'x_test_is_prime_basics__mutmut_7': x_test_is_prime_basics__mutmut_7, 
    'x_test_is_prime_basics__mutmut_8': x_test_is_prime_basics__mutmut_8, 
    'x_test_is_prime_basics__mutmut_9': x_test_is_prime_basics__mutmut_9
}

def x_test_is_prime_basics__mutmut_orig(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_basics__mutmut_orig, x_test_is_prime_basics__mutmut_mutants, *args, **kwargs)
    return result 

def x_test_is_prime_basics__mutmut_1(*args, **kwargs):
    result = _mutmut_trampoline(None, x_test_is_prime_basics__mutmut_mutants, *args, **kwargs)
    return result 

def x_test_is_prime_basics__mutmut_2(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_basics__mutmut_orig, None, *args, **kwargs)
    return result 

def x_test_is_prime_basics__mutmut_3(*args, **kwargs):
    result = _mutmut_trampoline( x_test_is_prime_basics__mutmut_mutants, *args, **kwargs)
    return result 

def x_test_is_prime_basics__mutmut_4(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_basics__mutmut_orig, *args, **kwargs)
    return result 

def x_test_is_prime_basics__mutmut_5(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_basics__mutmut_orig, x_test_is_prime_basics__mutmut_mutants, **kwargs)
    return result 

def x_test_is_prime_basics__mutmut_6(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_basics__mutmut_orig, x_test_is_prime_basics__mutmut_mutants, *args,)
    return result 

def x_test_is_prime_basics__mutmut_7(*args, **kwargs):
    result = None
    return result 

x_test_is_prime_basics__mutmut_mutants = {
'x_test_is_prime_basics__mutmut_1': x_test_is_prime_basics__mutmut_1, 
    'x_test_is_prime_basics__mutmut_2': x_test_is_prime_basics__mutmut_2, 
    'x_test_is_prime_basics__mutmut_3': x_test_is_prime_basics__mutmut_3, 
    'x_test_is_prime_basics__mutmut_4': x_test_is_prime_basics__mutmut_4, 
    'x_test_is_prime_basics__mutmut_5': x_test_is_prime_basics__mutmut_5, 
    'x_test_is_prime_basics__mutmut_6': x_test_is_prime_basics__mutmut_6, 
    'x_test_is_prime_basics__mutmut_7': x_test_is_prime_basics__mutmut_7
}

def test_is_prime_basics(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_basics__mutmut_orig, x_test_is_prime_basics__mutmut_mutants, *args, **kwargs)
    return result 

test_is_prime_basics.__signature__ = _mutmut_signature(x_test_is_prime_basics__mutmut_orig)
x_test_is_prime_basics__mutmut_orig.__name__ = 'x_test_is_prime_basics'



test_is_prime_basics.__signature__ = _mutmut_signature(x_test_is_prime_basics__mutmut_orig)
x_test_is_prime_basics__mutmut_orig.__name__ = 'x_test_is_prime_basics'



def x_x_test_is_prime_advanced__mutmut_orig__mutmut_orig():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-7)



def x_x_test_is_prime_advanced__mutmut_orig__mutmut_1():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-7)



def x_x_test_is_prime_advanced__mutmut_orig__mutmut_2():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert not is_prime(15)
  assert not is_prime(-7)



def x_x_test_is_prime_advanced__mutmut_orig__mutmut_3():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert  is_prime(15)
  assert not is_prime(-7)



def x_x_test_is_prime_advanced__mutmut_orig__mutmut_4():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(16)
  assert not is_prime(-7)



def x_x_test_is_prime_advanced__mutmut_orig__mutmut_5():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert  is_prime(-7)



def x_x_test_is_prime_advanced__mutmut_orig__mutmut_6():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(+7)



def x_x_test_is_prime_advanced__mutmut_orig__mutmut_7():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-8)

x_x_test_is_prime_advanced__mutmut_orig__mutmut_mutants = {
'x_x_test_is_prime_advanced__mutmut_orig__mutmut_1': x_x_test_is_prime_advanced__mutmut_orig__mutmut_1, 
    'x_x_test_is_prime_advanced__mutmut_orig__mutmut_2': x_x_test_is_prime_advanced__mutmut_orig__mutmut_2, 
    'x_x_test_is_prime_advanced__mutmut_orig__mutmut_3': x_x_test_is_prime_advanced__mutmut_orig__mutmut_3, 
    'x_x_test_is_prime_advanced__mutmut_orig__mutmut_4': x_x_test_is_prime_advanced__mutmut_orig__mutmut_4, 
    'x_x_test_is_prime_advanced__mutmut_orig__mutmut_5': x_x_test_is_prime_advanced__mutmut_orig__mutmut_5, 
    'x_x_test_is_prime_advanced__mutmut_orig__mutmut_6': x_x_test_is_prime_advanced__mutmut_orig__mutmut_6, 
    'x_x_test_is_prime_advanced__mutmut_orig__mutmut_7': x_x_test_is_prime_advanced__mutmut_orig__mutmut_7
}

def x_test_is_prime_advanced__mutmut_orig(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_advanced__mutmut_orig__mutmut_orig, x_x_test_is_prime_advanced__mutmut_orig__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_advanced__mutmut_orig.__signature__ = _mutmut_signature(x_x_test_is_prime_advanced__mutmut_orig__mutmut_orig)
x_x_test_is_prime_advanced__mutmut_orig__mutmut_orig.__name__ = 'x_x_test_is_prime_advanced__mutmut_orig'



def x_x_test_is_prime_advanced__mutmut_1__mutmut_orig():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_1__mutmut_1():
  # casos avancados e teste de fronteiras
  assert is_prime(13)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_1__mutmut_2():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(14)
  assert not is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_1__mutmut_3():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert  is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_1__mutmut_4():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert not is_prime(16)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_1__mutmut_5():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert not is_prime(15)
  assert  is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_1__mutmut_6():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_1__mutmut_7():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-8)

x_x_test_is_prime_advanced__mutmut_1__mutmut_mutants = {
'x_x_test_is_prime_advanced__mutmut_1__mutmut_1': x_x_test_is_prime_advanced__mutmut_1__mutmut_1, 
    'x_x_test_is_prime_advanced__mutmut_1__mutmut_2': x_x_test_is_prime_advanced__mutmut_1__mutmut_2, 
    'x_x_test_is_prime_advanced__mutmut_1__mutmut_3': x_x_test_is_prime_advanced__mutmut_1__mutmut_3, 
    'x_x_test_is_prime_advanced__mutmut_1__mutmut_4': x_x_test_is_prime_advanced__mutmut_1__mutmut_4, 
    'x_x_test_is_prime_advanced__mutmut_1__mutmut_5': x_x_test_is_prime_advanced__mutmut_1__mutmut_5, 
    'x_x_test_is_prime_advanced__mutmut_1__mutmut_6': x_x_test_is_prime_advanced__mutmut_1__mutmut_6, 
    'x_x_test_is_prime_advanced__mutmut_1__mutmut_7': x_x_test_is_prime_advanced__mutmut_1__mutmut_7
}

def x_test_is_prime_advanced__mutmut_1(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_advanced__mutmut_1__mutmut_orig, x_x_test_is_prime_advanced__mutmut_1__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_advanced__mutmut_1.__signature__ = _mutmut_signature(x_x_test_is_prime_advanced__mutmut_1__mutmut_orig)
x_x_test_is_prime_advanced__mutmut_1__mutmut_orig.__name__ = 'x_x_test_is_prime_advanced__mutmut_1'



def x_x_test_is_prime_advanced__mutmut_2__mutmut_orig():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert not is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_2__mutmut_1():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(14)
  assert not is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_2__mutmut_2():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(15)
  assert not is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_2__mutmut_3():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert  is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_2__mutmut_4():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert not is_prime(16)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_2__mutmut_5():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert not is_prime(15)
  assert  is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_2__mutmut_6():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert not is_prime(15)
  assert not is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_2__mutmut_7():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert not is_prime(15)
  assert not is_prime(-8)

x_x_test_is_prime_advanced__mutmut_2__mutmut_mutants = {
'x_x_test_is_prime_advanced__mutmut_2__mutmut_1': x_x_test_is_prime_advanced__mutmut_2__mutmut_1, 
    'x_x_test_is_prime_advanced__mutmut_2__mutmut_2': x_x_test_is_prime_advanced__mutmut_2__mutmut_2, 
    'x_x_test_is_prime_advanced__mutmut_2__mutmut_3': x_x_test_is_prime_advanced__mutmut_2__mutmut_3, 
    'x_x_test_is_prime_advanced__mutmut_2__mutmut_4': x_x_test_is_prime_advanced__mutmut_2__mutmut_4, 
    'x_x_test_is_prime_advanced__mutmut_2__mutmut_5': x_x_test_is_prime_advanced__mutmut_2__mutmut_5, 
    'x_x_test_is_prime_advanced__mutmut_2__mutmut_6': x_x_test_is_prime_advanced__mutmut_2__mutmut_6, 
    'x_x_test_is_prime_advanced__mutmut_2__mutmut_7': x_x_test_is_prime_advanced__mutmut_2__mutmut_7
}

def x_test_is_prime_advanced__mutmut_2(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_advanced__mutmut_2__mutmut_orig, x_x_test_is_prime_advanced__mutmut_2__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_advanced__mutmut_2.__signature__ = _mutmut_signature(x_x_test_is_prime_advanced__mutmut_2__mutmut_orig)
x_x_test_is_prime_advanced__mutmut_2__mutmut_orig.__name__ = 'x_x_test_is_prime_advanced__mutmut_2'



def x_x_test_is_prime_advanced__mutmut_3__mutmut_orig():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert  is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_3__mutmut_1():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert  is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_3__mutmut_2():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert  is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_3__mutmut_3():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert  is_prime(16)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_3__mutmut_4():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert  is_prime(15)
  assert  is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_3__mutmut_5():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert  is_prime(15)
  assert not is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_3__mutmut_6():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert  is_prime(15)
  assert not is_prime(-8)

x_x_test_is_prime_advanced__mutmut_3__mutmut_mutants = {
'x_x_test_is_prime_advanced__mutmut_3__mutmut_1': x_x_test_is_prime_advanced__mutmut_3__mutmut_1, 
    'x_x_test_is_prime_advanced__mutmut_3__mutmut_2': x_x_test_is_prime_advanced__mutmut_3__mutmut_2, 
    'x_x_test_is_prime_advanced__mutmut_3__mutmut_3': x_x_test_is_prime_advanced__mutmut_3__mutmut_3, 
    'x_x_test_is_prime_advanced__mutmut_3__mutmut_4': x_x_test_is_prime_advanced__mutmut_3__mutmut_4, 
    'x_x_test_is_prime_advanced__mutmut_3__mutmut_5': x_x_test_is_prime_advanced__mutmut_3__mutmut_5, 
    'x_x_test_is_prime_advanced__mutmut_3__mutmut_6': x_x_test_is_prime_advanced__mutmut_3__mutmut_6
}

def x_test_is_prime_advanced__mutmut_3(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_advanced__mutmut_3__mutmut_orig, x_x_test_is_prime_advanced__mutmut_3__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_advanced__mutmut_3.__signature__ = _mutmut_signature(x_x_test_is_prime_advanced__mutmut_3__mutmut_orig)
x_x_test_is_prime_advanced__mutmut_3__mutmut_orig.__name__ = 'x_x_test_is_prime_advanced__mutmut_3'



def x_x_test_is_prime_advanced__mutmut_4__mutmut_orig():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(16)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_4__mutmut_1():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert not is_prime(16)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_4__mutmut_2():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert not is_prime(16)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_4__mutmut_3():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert  is_prime(16)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_4__mutmut_4():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(17)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_4__mutmut_5():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(16)
  assert  is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_4__mutmut_6():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(16)
  assert not is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_4__mutmut_7():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(16)
  assert not is_prime(-8)

x_x_test_is_prime_advanced__mutmut_4__mutmut_mutants = {
'x_x_test_is_prime_advanced__mutmut_4__mutmut_1': x_x_test_is_prime_advanced__mutmut_4__mutmut_1, 
    'x_x_test_is_prime_advanced__mutmut_4__mutmut_2': x_x_test_is_prime_advanced__mutmut_4__mutmut_2, 
    'x_x_test_is_prime_advanced__mutmut_4__mutmut_3': x_x_test_is_prime_advanced__mutmut_4__mutmut_3, 
    'x_x_test_is_prime_advanced__mutmut_4__mutmut_4': x_x_test_is_prime_advanced__mutmut_4__mutmut_4, 
    'x_x_test_is_prime_advanced__mutmut_4__mutmut_5': x_x_test_is_prime_advanced__mutmut_4__mutmut_5, 
    'x_x_test_is_prime_advanced__mutmut_4__mutmut_6': x_x_test_is_prime_advanced__mutmut_4__mutmut_6, 
    'x_x_test_is_prime_advanced__mutmut_4__mutmut_7': x_x_test_is_prime_advanced__mutmut_4__mutmut_7
}

def x_test_is_prime_advanced__mutmut_4(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_advanced__mutmut_4__mutmut_orig, x_x_test_is_prime_advanced__mutmut_4__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_advanced__mutmut_4.__signature__ = _mutmut_signature(x_x_test_is_prime_advanced__mutmut_4__mutmut_orig)
x_x_test_is_prime_advanced__mutmut_4__mutmut_orig.__name__ = 'x_x_test_is_prime_advanced__mutmut_4'



def x_x_test_is_prime_advanced__mutmut_5__mutmut_orig():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert  is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_5__mutmut_1():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert not is_prime(15)
  assert  is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_5__mutmut_2():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert not is_prime(15)
  assert  is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_5__mutmut_3():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert  is_prime(15)
  assert  is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_5__mutmut_4():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(16)
  assert  is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_5__mutmut_5():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert  is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_5__mutmut_6():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert  is_prime(-8)

x_x_test_is_prime_advanced__mutmut_5__mutmut_mutants = {
'x_x_test_is_prime_advanced__mutmut_5__mutmut_1': x_x_test_is_prime_advanced__mutmut_5__mutmut_1, 
    'x_x_test_is_prime_advanced__mutmut_5__mutmut_2': x_x_test_is_prime_advanced__mutmut_5__mutmut_2, 
    'x_x_test_is_prime_advanced__mutmut_5__mutmut_3': x_x_test_is_prime_advanced__mutmut_5__mutmut_3, 
    'x_x_test_is_prime_advanced__mutmut_5__mutmut_4': x_x_test_is_prime_advanced__mutmut_5__mutmut_4, 
    'x_x_test_is_prime_advanced__mutmut_5__mutmut_5': x_x_test_is_prime_advanced__mutmut_5__mutmut_5, 
    'x_x_test_is_prime_advanced__mutmut_5__mutmut_6': x_x_test_is_prime_advanced__mutmut_5__mutmut_6
}

def x_test_is_prime_advanced__mutmut_5(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_advanced__mutmut_5__mutmut_orig, x_x_test_is_prime_advanced__mutmut_5__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_advanced__mutmut_5.__signature__ = _mutmut_signature(x_x_test_is_prime_advanced__mutmut_5__mutmut_orig)
x_x_test_is_prime_advanced__mutmut_5__mutmut_orig.__name__ = 'x_x_test_is_prime_advanced__mutmut_5'



def x_x_test_is_prime_advanced__mutmut_6__mutmut_orig():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_6__mutmut_1():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_6__mutmut_2():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert not is_prime(15)
  assert not is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_6__mutmut_3():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert  is_prime(15)
  assert not is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_6__mutmut_4():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(16)
  assert not is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_6__mutmut_5():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert  is_prime(+7)

def x_x_test_is_prime_advanced__mutmut_6__mutmut_6():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-7)

def x_x_test_is_prime_advanced__mutmut_6__mutmut_7():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(+8)

x_x_test_is_prime_advanced__mutmut_6__mutmut_mutants = {
'x_x_test_is_prime_advanced__mutmut_6__mutmut_1': x_x_test_is_prime_advanced__mutmut_6__mutmut_1, 
    'x_x_test_is_prime_advanced__mutmut_6__mutmut_2': x_x_test_is_prime_advanced__mutmut_6__mutmut_2, 
    'x_x_test_is_prime_advanced__mutmut_6__mutmut_3': x_x_test_is_prime_advanced__mutmut_6__mutmut_3, 
    'x_x_test_is_prime_advanced__mutmut_6__mutmut_4': x_x_test_is_prime_advanced__mutmut_6__mutmut_4, 
    'x_x_test_is_prime_advanced__mutmut_6__mutmut_5': x_x_test_is_prime_advanced__mutmut_6__mutmut_5, 
    'x_x_test_is_prime_advanced__mutmut_6__mutmut_6': x_x_test_is_prime_advanced__mutmut_6__mutmut_6, 
    'x_x_test_is_prime_advanced__mutmut_6__mutmut_7': x_x_test_is_prime_advanced__mutmut_6__mutmut_7
}

def x_test_is_prime_advanced__mutmut_6(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_advanced__mutmut_6__mutmut_orig, x_x_test_is_prime_advanced__mutmut_6__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_advanced__mutmut_6.__signature__ = _mutmut_signature(x_x_test_is_prime_advanced__mutmut_6__mutmut_orig)
x_x_test_is_prime_advanced__mutmut_6__mutmut_orig.__name__ = 'x_x_test_is_prime_advanced__mutmut_6'



def x_x_test_is_prime_advanced__mutmut_7__mutmut_orig():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-8)

def x_x_test_is_prime_advanced__mutmut_7__mutmut_1():
  # casos avancados e teste de fronteiras
  assert is_prime(12)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-8)

def x_x_test_is_prime_advanced__mutmut_7__mutmut_2():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(14)
  assert not is_prime(15)
  assert not is_prime(-8)

def x_x_test_is_prime_advanced__mutmut_7__mutmut_3():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert  is_prime(15)
  assert not is_prime(-8)

def x_x_test_is_prime_advanced__mutmut_7__mutmut_4():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(16)
  assert not is_prime(-8)

def x_x_test_is_prime_advanced__mutmut_7__mutmut_5():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert  is_prime(-8)

def x_x_test_is_prime_advanced__mutmut_7__mutmut_6():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(+8)

def x_x_test_is_prime_advanced__mutmut_7__mutmut_7():
  # casos avancados e teste de fronteiras
  assert is_prime(11)
  assert is_prime(13)
  assert not is_prime(15)
  assert not is_prime(-9)

x_x_test_is_prime_advanced__mutmut_7__mutmut_mutants = {
'x_x_test_is_prime_advanced__mutmut_7__mutmut_1': x_x_test_is_prime_advanced__mutmut_7__mutmut_1, 
    'x_x_test_is_prime_advanced__mutmut_7__mutmut_2': x_x_test_is_prime_advanced__mutmut_7__mutmut_2, 
    'x_x_test_is_prime_advanced__mutmut_7__mutmut_3': x_x_test_is_prime_advanced__mutmut_7__mutmut_3, 
    'x_x_test_is_prime_advanced__mutmut_7__mutmut_4': x_x_test_is_prime_advanced__mutmut_7__mutmut_4, 
    'x_x_test_is_prime_advanced__mutmut_7__mutmut_5': x_x_test_is_prime_advanced__mutmut_7__mutmut_5, 
    'x_x_test_is_prime_advanced__mutmut_7__mutmut_6': x_x_test_is_prime_advanced__mutmut_7__mutmut_6, 
    'x_x_test_is_prime_advanced__mutmut_7__mutmut_7': x_x_test_is_prime_advanced__mutmut_7__mutmut_7
}

def x_test_is_prime_advanced__mutmut_7(*args, **kwargs):
    result = _mutmut_trampoline(x_x_test_is_prime_advanced__mutmut_7__mutmut_orig, x_x_test_is_prime_advanced__mutmut_7__mutmut_mutants, *args, **kwargs)
    return result 

x_test_is_prime_advanced__mutmut_7.__signature__ = _mutmut_signature(x_x_test_is_prime_advanced__mutmut_7__mutmut_orig)
x_x_test_is_prime_advanced__mutmut_7__mutmut_orig.__name__ = 'x_x_test_is_prime_advanced__mutmut_7'



x_test_is_prime_advanced__mutmut_mutants = {
'x_test_is_prime_advanced__mutmut_1': x_test_is_prime_advanced__mutmut_1, 
    'x_test_is_prime_advanced__mutmut_2': x_test_is_prime_advanced__mutmut_2, 
    'x_test_is_prime_advanced__mutmut_3': x_test_is_prime_advanced__mutmut_3, 
    'x_test_is_prime_advanced__mutmut_4': x_test_is_prime_advanced__mutmut_4, 
    'x_test_is_prime_advanced__mutmut_5': x_test_is_prime_advanced__mutmut_5, 
    'x_test_is_prime_advanced__mutmut_6': x_test_is_prime_advanced__mutmut_6, 
    'x_test_is_prime_advanced__mutmut_7': x_test_is_prime_advanced__mutmut_7
}

def x_test_is_prime_advanced__mutmut_orig(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_advanced__mutmut_orig, x_test_is_prime_advanced__mutmut_mutants, *args, **kwargs)
    return result 

def x_test_is_prime_advanced__mutmut_1(*args, **kwargs):
    result = _mutmut_trampoline(None, x_test_is_prime_advanced__mutmut_mutants, *args, **kwargs)
    return result 

def x_test_is_prime_advanced__mutmut_2(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_advanced__mutmut_orig, None, *args, **kwargs)
    return result 

def x_test_is_prime_advanced__mutmut_3(*args, **kwargs):
    result = _mutmut_trampoline( x_test_is_prime_advanced__mutmut_mutants, *args, **kwargs)
    return result 

def x_test_is_prime_advanced__mutmut_4(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_advanced__mutmut_orig, *args, **kwargs)
    return result 

def x_test_is_prime_advanced__mutmut_5(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_advanced__mutmut_orig, x_test_is_prime_advanced__mutmut_mutants, **kwargs)
    return result 

def x_test_is_prime_advanced__mutmut_6(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_advanced__mutmut_orig, x_test_is_prime_advanced__mutmut_mutants, *args,)
    return result 

def x_test_is_prime_advanced__mutmut_7(*args, **kwargs):
    result = None
    return result 

x_test_is_prime_advanced__mutmut_mutants = {
'x_test_is_prime_advanced__mutmut_1': x_test_is_prime_advanced__mutmut_1, 
    'x_test_is_prime_advanced__mutmut_2': x_test_is_prime_advanced__mutmut_2, 
    'x_test_is_prime_advanced__mutmut_3': x_test_is_prime_advanced__mutmut_3, 
    'x_test_is_prime_advanced__mutmut_4': x_test_is_prime_advanced__mutmut_4, 
    'x_test_is_prime_advanced__mutmut_5': x_test_is_prime_advanced__mutmut_5, 
    'x_test_is_prime_advanced__mutmut_6': x_test_is_prime_advanced__mutmut_6, 
    'x_test_is_prime_advanced__mutmut_7': x_test_is_prime_advanced__mutmut_7
}

def test_is_prime_advanced(*args, **kwargs):
    result = _mutmut_trampoline(x_test_is_prime_advanced__mutmut_orig, x_test_is_prime_advanced__mutmut_mutants, *args, **kwargs)
    return result 

test_is_prime_advanced.__signature__ = _mutmut_signature(x_test_is_prime_advanced__mutmut_orig)
x_test_is_prime_advanced__mutmut_orig.__name__ = 'x_test_is_prime_advanced'



test_is_prime_advanced.__signature__ = _mutmut_signature(x_test_is_prime_advanced__mutmut_orig)
x_test_is_prime_advanced__mutmut_orig.__name__ = 'x_test_is_prime_advanced'


