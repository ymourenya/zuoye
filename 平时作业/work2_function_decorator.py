import random
import string


# 函数修饰器
def ml_method(method_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 执行机器学习方法
            print("Running machine learning method:", method_name)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def evaluation_metric(metric_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 执行精度指标操作
            print("Running evaluation metric:", metric_name)
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@ml_method("RNN")
@evaluation_metric("RECALL")
def dataSampling(**kwargs):
    result = []
    for key, value in kwargs.items():
        if key == 'int':
            result.append(random.randint(0, value))
        elif key == 'float':
            result.append(random.uniform(0, value))
        elif key == 'str':
            length = value
            result.append(''.join(random.choices(string.ascii_letters + string.digits, k=length)))
    return result


print(dataSampling(int=100, float=10.0, str=5))
