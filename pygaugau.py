import requests
#print(requests.get('https://google.com'))




# print("Đang vào tool...",'\r')


import sys
import random
import ast
import zlib
import marshal
import base64
import bz2
from pystyle import *
class DepTraiCoGiSai(ExceptionGroup):0
class GHIᅠCHÚ(MemoryError):0
if sys.version_info < (3, 10):
    print("Install Python Version = 3.10 or > 3.10 To Use This Code ")
    sys.exit()

def _rd():
    return "".join(__import__("random").sample(
        [chr(i) for i in range(97, 122)], k=5))


def _rd1():
    return "".join(__import__("random").sample(
        [chr(i) for i in range(97, 122)], k=1))


def rd():
    # return "_" + "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))
    return ''.join(__import__('random').choices([chr(i) for i in range(0x4e00, 0x9fff)], k=3))
    #return ''.join(__import__('random').choices([chr(i) for i in range(65, 90)], k=22))


def rd2():
    # return "_" + "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))
    return ''.join(__import__('random').choices([chr(i) for i in range(0x4e00, 0x9fff)], k=4))

def superrandom():
    # return "_" + "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))
    return ''.join(__import__('random').choices([chr(i) for i in range(1000, 3000)], k=1503))

def rditerger():
    return "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))




def _chrobf(x):
    return ord(x) + int(zlib.decompress(b'x\x9c36&\x17\x18\x99\x00!:0\x87P\xc6\xc6\x00\x0bx\x11v'))


def obfstr(v):
    global _join
    global _hexrun
    global obfint
    if v == "":
        return f"''"
    else:
        x = []
        r = list(v)
        for i in range(len(r)):
            x.append(_chrobf(r[i]))
        _str_ = f"(lambda  : (lambda : (lambda : {_join}(( {_list}({_map}({_hexrun}, {x})) )))())())()"
        return _str_


def randomchar():
    return random.sample(['<','>','==',],k=1)[0]

hexspam = f"""
"""
 

antipycdc = ''

def antibypass():
    def anti(s: str, kkk=69):
        def f(n):
            a, b = n & 0b11110000, n & 0b00001111
            return f"(({a+10000000000000000000000000}) >>  ({b+100000000000000000000000000000000000}))" if n > 15 else str(n)
        fx = [f(ord(c) ^ kkk) for c in s]
        mm = ", ".join(fx)
        return f"""((lambda __thesmartdog__: __thesmartdog__(*[__dat__('HELLO DECOMPILER',{mm})]))(lambda *__datcute__: ((lambda __wearelove__, __uyencoder__:__wearelove__().join([*map(lambda n: __uyencoder__().format((n ^ 64)), __datcute__)]))(lambda: getattr(''.__class__, '__add__')('__dat__', ''),lambda: "__yeuquynhngan__"))))"""

    def _anti():
        antipycdc = ''
        for i in range(1000):
            antipycdc += f"__uyencoderdeptrai__(__uyencoderdeptrai__(__uyencoderdeptrai__(__uyencoderdeptrai__(__uyencoderdeptrai__(__uyencoderdeptrai__('')))))),"
        antipycdc = "try:thesmartdog=[" + antipycdc + "]\nexcept:pass"
        txf = f"""
def __uyencoderdeptrai__(__deptrai__):
    return __deptrai__

try:pass
except:pass
finally:pass
{antipycdc}
finally:int(2008-2006)
        """
        return f"""
try:
    def __dat__(__ok__):return "__ANTI DECOMPILER__"
    {anti("__thesmartdog__")}
except:pass
else:pass
finally:pass
{txf}"""

    return _anti()

ANTI_PYCDC = f"""
{antibypass()}
"""
# ANTI_PYCDC = ''


import random
# def obfstr(string):
#     global _hexrun
#     global _join
#     keys = []
#     magic = random.randint(1000000, 9999999)
#     for char in string:
#         logic = random.randint(1, 4)
#         if logic == 1:
#             logic = '+'
#         elif logic == 2:
#             logic = '*'
#         elif logic == 3:
#             logic = '<<'
#         else:
#             logic = '^'
        
#         key = ord(char) + 3333333333333333333333333333333333333333333333333333333333242422222222222222222722222233    
#         key2 = magic
        
#         if logic == "^":
#             key3 = ~key ^ ~magic
#             keys.append(f"(lambda: {_hexrun}({key2} ^ {key3}))()")
#         elif logic == "<<":
#             magic = random.randint(1, 19)
#             key3 = key << magic
#             PT = ">>"
#             keys.append(f"(lambda: {_hexrun}({key3} {PT} {magic}))()")
#         else:
#             if logic == "+":
#                 PT = "-"
#             else:
#                 PT = "//"
#             key3 = eval(f"{key} {logic} {magic}")
#             keys.append(f"(lambda: {_hexrun}({key3} {PT} {key2}))()")
    
#     return f"(lambda: {_join}([{', '.join(keys)}]))()"


def _byte(v):
    byte_array = bytearray()
    byte_array.extend(v.to_bytes((v.bit_length() + 7) // 8, 'big'))
    return b"0xFFFFFFFF/" + byte_array

def obfint(v):
    n = rd()
    global _idk
    if 'bool' in str(type(v)):
        if str(v)=='True':
            return f'(lambda: (lambda {n}: {n} + (lambda : {vaicalon}({(1+0xFFFFFFFFFFFFFFFFFFFFFF)}))())(0) == 1)()'
        else:
            return f'(lambda: (lambda {n}: {n} - (lambda : {vaicalon}(({(1+0xFFFFFFFFFFFFFFFFFFFFFF)} ) ) )())(0) == 1)()'
    else:
        #return f"""{vaicalon}({(v+0xFFFFFFFFFFFFFFFFFFFFFF)}) if {_str}({_type}({_bool}({vaicalon}({(v+0xFFFFFFFFFFFFFFFFFFFFFF)})))) == {_str}({_type}({_int}({rditerger()})>{_int}({rditerger()})<{_int}({rditerger()})>{_int}({rditerger()}))) else {vaicalon}({v+0xFFFFFFFFFFFFFFFFFFFFFF})"""
        #return f"""(lambda {rd()} : {vaicalon}({(v+0xFFFFFFFFFFFFFFFFFFFFFF)})("datchuche")"""
        #return f"""(lambda : {vaicalon}({(v+0xFFFFFFFFFFFFFFFFFFFFFF)})//eval({obfstr('1')}))()"""
        #print(fr""" unhexlify('{_byte(int(v))}') """)
        #return fr"""(lambda : """
        return f'(lambda: {_idk}({_byte(int(v))}))()'


def varsobf(v):
    #return f"""({nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()]) if {nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()]({nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()]({nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()]({(v)}))) < {nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()]({nuyenbuiltins}['type']({nuyenbuiltins}['int']({rditerger()})>{nuyenbuiltins}['int']({rditerger()})<{nuyenbuiltins}['int']({rditerger()})>{nuyenbuiltins}['int']({rditerger()}))) and {nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()](str(str({rditerger()})>{nuyenbuiltins}['int']({rditerger()})<{nuyenbuiltins}['int']({rditerger()})>{nuyenbuiltins}['int']({rditerger()}))) > 2 else {v}"""
    global array
    deptrai = list(v)[::-1]
    holly=[]
    for i in deptrai:
        holly.append(f"(lambda : {array}('{superrandom()}{superrandom()}{i}'))()")
    return '+'.join(holly)




_join = rd()
_int = rd()
_str = rd()
_bool = rd()
_type = rd()
_bytes = rd()
_vars = rd()
array = rd()
_ip = rd()
_bytearray = rd()
vaicalon = rd()
___import__ = rd()
_movdiv = rd()
_hexrun = rd()
_argshexrun = rd()
_eval = rd()
_list = rd()
_map = rd()
_idk = rd()
nuyenbuiltins = rd()
_memoryerror = rd()
rpq = rd()
__print = r"tryᅠ"
__input = r"exceptᅠ"
# variables = [
#     '_join', '_int', '_str', '_bool', '_type', '_bytes', '_vars', '_ip', 'vaicalon', 
#     '__import__', 'movdiv', 'hexrun', 'argshexrun', 'eval', 'list', 'map', 
#     'idk', 'nuyenbuiltins', 'memoryerror'
# ]
# for var_name in variables:
#     globals()[var_name] = rd()
def unicodeobf(x):
    b = []
    for i in x:
        j = ord(i) + int(zlib.decompress(b'x\x9c36&\x17\x18\x99\x00!:0\x87P\xc6\xc6\x00\x0bx\x11v'))
        b.append(j)
    return b


def _uni(x):
    return unicodeobf(x)
# def makelambda(string):
#     num_loops = 25
#     lambda_str = "lambda: " + repr(string)
#     for _ in range(num_loops):
#         lambda_str = "lambda: (" + lambda_str + ")()"
    
#     return lambda_str + "()"
utf8 = rd()
__bool = rd()
__exx = rd()
_temp = rd()
_temp1 = rd()
_wt = rd()
_exp = rd()
_meh = rd()
_globals = rd()
_len = rd()
var = fr"""
try:
    class {_memoryerror}(eval("Exception")):_ : (lambda :"Tao la dat dep trai")();pass
except Exeption as TUOI_LON_DECODE:pass
else:globals()["dec_dec_cái_đầu_buồi"] = "BỐ ĐẠT"
finally:
    {utf8} = "utf8"
    {_globals} = globals()
{array} = lambda {array}: {array}[(lambda : -1)()]
def {_join}({_wt}):
    {__exx} = ""
    for {_globals}['{_temp1}'], {_globals}['{_temp}'] in enumerate({_wt}):
        if {_globals}['{_temp1}'] > 0:
            {__exx} += ""
        {__exx} += str({_globals}['{_temp}'])
    return {__exx}
{nuyenbuiltins} = vars(globals()['__builtins__'])
{_eval} =  eval({_join}({varsobf('eval')})[::-1])
{_bool} = {_eval}({_join}({varsobf('bool')})[::-1])
{_str} =  {_eval}({_join}({varsobf('str')})[::-1])
{_type} =  {_eval}({_join}({varsobf('type')})[::-1])
{_int} =  {_eval}({_join}({varsobf('int')})[::-1])
{_bytes} =  {_eval}({_join}({varsobf('bytes')})[::-1])
{_vars} =  {_eval}({_join}({varsobf('vars')})[::-1])
{_movdiv} =  {_eval}({_join}({varsobf('callable')})[::-1])
{_list} =  {_eval}({_join}({varsobf('list')})[::-1])
{_map} =  {_eval}({_join}({varsobf('map')})[::-1])
{___import__} =  {_eval}({_join}({varsobf('__import__')})[::-1])
{_bytearray} = {_eval}({_join}({varsobf('bytearray')})[::-1])
{_len} = {_eval}({_join}({varsobf('len')})[::-1])

exceptᅠ =  {_eval}({_join}({varsobf('input')})[::-1])
def {_join}({__exx},*k):
    if k:
        {_meh} = '+'
        op = "+"
    else:
        {_meh} = ''
        op = ''
    {_globals}['{__exx}'] = {obfint(True)}
    {_globals}['{_join}'] = {_join}
    {_globals}['{_str}'] = {_str}
    {_globals}['{__exx}'] = {__exx}
    for {_globals}['{_meh}_'] in {_globals}['{__exx}']:
        if not {__exx}:{_globals}['{_meh}_'] += (lambda : '')()
        {_meh} += {_str}({_meh}_)
    return {_meh}
def {vaicalon}({_wt}):
    return {_int}({_wt}-0xFFFFFFFFFFFFFFFFFFFFFF)
def {_idk}({_wt}):
    {__exx} = {_bytearray}({_wt}[{_len}(b'0xFFFFFFFF/'):])
    {_temp} = 0
    for {_temp1} in {__exx}:
        {_temp} = {_temp} * 256 + {_temp1}
    return {_temp}
def {_hexrun}({_argshexrun}):
    {_argshexrun} = {_argshexrun}-3333333333333333333333333333333333333333333333333333333333242422222222222222222722222233  
    if {_argshexrun} <= 0x7F:
                return {_str}({_bytes}([{_argshexrun}]),{utf8})
    elif {_argshexrun} <= 0x7FF:
                if 1<2:
                        {_globals}['{_temp}'] = 0xC0 | ({_argshexrun} >> 6)
                {_globals}['{_temp1}'] = 0x80 | ({_argshexrun} & 0x3F)
                return {_str}({_bytes}([{_globals}['{_temp}'], {_globals}['{_temp1}']]),{utf8})
    elif {_argshexrun} <= 0xFFFF:
            {_globals}['{_temp}'] = 0xE0 | ({_argshexrun} >> 12)
            if 2>1:
                {_globals}['{_temp1}'] = 0x80 | (({_argshexrun} >> 6) & 0x3F)
            {_globals}['{_wt}'] = 0x80 | ({_argshexrun} & 0x3F)
            return {_str}({_bytes}([{_globals}['{_temp}'], {_globals}['{_temp1}'], {_globals}['{_wt}']]),{utf8})
    else:
        {_globals}['{_temp}'] = 0xF0 | ({_argshexrun} >> 18)
        if 2==2:
            {_globals}['{_temp1}'] = 0x80 | (({_argshexrun} >> 12) & 0x3F)
        if 1<2<3:
            {_globals}['{_wt}'] = 0x80 | (({_argshexrun} >> 6) & 0x3F)
        {_globals}['{_exp}'] = 0x80 | ({_argshexrun} & 0x3F)
        return {_str}({_bytes}([{_globals}['{_temp}'], {_globals}['{_temp1}'], {_globals}['{_wt}'], {_globals}['{_exp}']]),{utf8})


tryᅠ = {_eval}({_join}({varsobf('print')})[::-1])
"""

dell = f"""

__import__('sys').exit()
__import__('sys').exit()
"""
import ast
def _moreobf(tree):
    import random


    def junk(en, max_value):
        cases = []
        line = max_value + 1
        for i in range(random.randint(1, 5)):
            case_name = "__"+rd()
            case_body = [
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=line)]
                    ), 
                    body=[
                        ast.Assign(
                            targets=[ast.Name(id=case_name)], 
                            value=ast.Constant(value=random.randint(0xFFFFF, 0xFFFFFFFFFFFF)), 
                            lineno=None
                        )
                    ], 
                    orelse=[]
                )
            ]
            cases.extend(case_body)
            line += 1
        return cases

    def bl(body):
        var = "__"+rd()
        en = "__"+rd()

        tb = [
            ast.AugAssign(
                target=ast.Name(id=var), 
                op=ast.Add(), 
                value=ast.Constant(value=1)
            ),
            ast.Try(
                body=[
                    ast.Raise(
                        exc=ast.Call(func=ast.Name(id=_memoryerror), 
                                     args=[ast.Name(id=var)], 
                                     keywords=[])
                    )
                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id=_memoryerror), 
                        name=en, 
                        body=[]
                    )
                ],
                orelse=[],
                finalbody=[]
            )
        ]
        
        for i in body:
            tb[1].handlers[0].body.append(
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=1)]
                    ), 
                    body=[i], 
                    orelse=[]
                )
            )
        
        tb[1].handlers[0].body.extend(junk(en, len(body) + 1))
        
        node = ast.Assign(
            targets=[ast.Name(id=var)], 
            value=ast.Constant(value=0), 
            lineno=None
        )
        
        return [node] + tb

    def _bl(node):
        olb = node.body

        var = rd()
        en = rd()

        tb = [
            ast.AugAssign(
                target=ast.Name(id=var), 
                op=ast.Add(), 
                value=ast.Constant(value=1)
            ),
            ast.Try(
                body=[
                    ast.Raise(
                        exc=ast.Call(func=ast.Name(id=_memoryerror), 
                                     args=[ast.Name(id=var)], 
                                     keywords=[])
                    )
                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id=_memoryerror), 
                        name=en, 
                        body=[]
                    )
                ],
                orelse=[],
                finalbody=[]
            )
        ]
        for i in olb:
            tb[1].handlers[0].body.append(
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=1)]
                    ), 
                    body=[i], 
                    orelse=[]
                )
            )
        tb[1].handlers[0].body.extend(junk(en, len(olb) + 1))
        node.body = [
            ast.Assign(
                targets=[ast.Name(id=var)], 
                value=ast.Constant(value=0), 
                lineno=None
            )
        ] + tb
        return node
    def on(node):
        if isinstance(node, ast.FunctionDef):
            return _bl(node)
        return node
    nb = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            nb.append(on(node))
        elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            nb.extend(bl([node]))
        elif isinstance(node, ast.Expr):
            nb.extend(bl([node]))
        else:
            nb.append(node)
    tree.body = nb
    return tree


def __moreobf(x):
    return ast.unparse(_moreobf(ast.parse(x)))

def fm(node: ast.JoinedStr) -> ast.Call:
    return ast.Call(
        func=ast.Attribute(
            value=ast.Constant(value="{}" * len(node.values)),
            attr="format",
            ctx=ast.Load(),
        ),
        args=[
            value.value if isinstance(value, ast.FormattedValue) else value
            for value in node.values
        ],
        keywords=[],
    )

def _syntax(x):
    def v(node):
        if node.name:
            for statement in node.body:
                ten = ast.Try(
                    body=[ast.parse(f"{_eval}('0/0')"),ast.parse(f"""if "ngocuyen" == "deptrai":{rd()},{rd()},{rd()},{rd()}\nelse:pass""")],
                    handlers=[
                        ast.ExceptHandler(
                            type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()),
                            name=None,
                            body=[z(statement)]
                        )
                    ],
                    orelse=[],
                    finalbody=[]
                )
                node.body[node.body.index(statement)] = ten
            return node
    def z(statement):
        return ast.Try(
            body=[ast.parse(f"{_eval}('0/0')")],
            handlers=[
                ast.ExceptHandler(
                    type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()),
                    name=None,
                    body=[statement]
                )
            ],
            orelse=[ast.Pass()],
            finalbody=[ast.parse("str(100)")]
        )
    tree = ast.parse(x)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            v(node)
    st = ast.unparse(tree)
    return st
ggg = print
dark = Col.dark_gray
light = Col.light_gray
purple = Colors.StaticMIX((Col.purple, Col.red))
bpurple = Colors.StaticMIX((Col.pink, Col.blue, Col.blue))

def stage(text: str, symbol: str = 'PYGAUGAU PREMIUM V1.1', col1 = light, col2 = None) -> str:
    if col2 is None:
        col2 = light if symbol == 'PYGAUGAU PREMIUM V1.1' else purple
    return f""" {Col.Symbol(symbol, col1, dark)} {Colorate.Diagonal(Colors.DynamicMIX((Col.red, light)), text)}{light}"""
def print1(x, *args, **kwargs):
    return _v(stage(x), *args, **kwargs)

def check(func):
    def okene(*args, **kwargs):
        okene.calls += 1
        return func(*args, **kwargs)
    okene.calls = 0
    return okene
def obfuscate(node):
    all_nodes = list(ast.walk(node))
    tt = sum(len(list(ast.iter_fields(n))) for n in all_nodes if not isinstance(n, (ast.Global, ast.Nonlocal)))
    iff = 0
    t = []
    for i in ast.walk(node):
        if isinstance(i, (ast.Global, ast.Nonlocal)):
            continue

        for f, v in ast.iter_fields(i):
            if isinstance(v, list):
                ar = []
                for j in v:
                    try:
                        if isinstance(j, ast.Constant) and isinstance(j.value, str):
                            ar.append(ast.parse(obfstr(j.value)).body[0].value)
                        elif isinstance(j, ast.Constant) and isinstance(j.value, int):
                            ar.append(ast.parse(obfint(j.value)).body[0].value)
                        elif isinstance(j, ast.JoinedStr):
                            ar.append(fm(j))
                        elif isinstance(j, ast.AST):
                            ar.append(j)
                    except Exception as e:
                        print(f"Error processing node {j}: {e}")
                        ar.append(j)
                setattr(i, f, ar)
            else:
                try:
                    if isinstance(v, ast.Constant) and isinstance(v.value, str):
                        setattr(i, f, ast.parse(obfstr(v.value)).body[0].value)
                    elif isinstance(v, ast.Constant) and isinstance(v.value, int):
                        setattr(i, f, ast.parse(obfint(v.value)).body[0].value)
                    elif isinstance(v, ast.JoinedStr):
                        setattr(i, f, fm(v))
                except Exception as e:
                    print(f"Error processing field {f} with value {v}: {e}")
            #iff += 1
            #if obfuscate.calls == 1:
            #    print1(f" CHECKING CODE {iff / tt * 100:.2f}%..      ", end='\r')
            #    if iff / tt * 100 == 100:
            #        print1(f" LOADING OBFUSCATION 0%..              ", end='\r')
            #if obfuscate.calls == 2:
            #    print1(f" LOADING OBFUSCATION {iff / tt * 100:.2f}%..              ", end='\r')
                

def rename_function(node, ol, nn):
    for i in ast.walk(node):
        if isinstance(i, ast.FunctionDef) and i.name == ol:
            i.name = nn
        elif isinstance(i, ast.Attribute) and isinstance(i.value, ast.Name) and i.value.id == ol:
            i.value.id = nn
        elif isinstance(i, ast.Call) and isinstance(i.func, ast.Name) and i.func.id == ol:
            i.func.id = nn
        elif isinstance(i, ast.Name) and i.id == ol:
            i.id = nn
    return node

def random_match_case():
    var1 = ast.Constant(value=rd(), kind=None)
    var2 = ast.Constant(value=rd(), kind=None)
    return ast.Match(
        subject=ast.Compare(
            left=var1,
            ops=[ast.Eq()],
            comparators=[var2],
        ),
        cases=[
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)),
                body=[
                    ast.Assign(
                        lineno=0,
                        col_offset=0,
                        targets=[],
                        value=[ast.Raise(
                    exc=ast.Call(
                        func=ast.Name(id=_memoryerror, ctx=ast.Load()),
                        args=[],
                        keywords=[],
                    ),)],
                    )
                ],
            ),
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=False, kind=None)),
                body=[
                    ast.Assign(
                        lineno=0,
                        col_offset=0,
                        targets=[ast.Name(id=rd(), ctx=ast.Store())],
                        value=ast.Constant(value=[[True], [False]], kind=None),
                    ),
                    ast.Expr(
                        lineno=0,
                        col_offset=0,
                        value=ast.Call(
                            func=ast.Name(id=_str, ctx=ast.Load()),
                            args=[ast.Constant(value=[rd()], kind=None)],
                            keywords=[],
                        ),
                    ),
                ],
            ),
        ],
    )


def trycatch(body, loop):
    ar = []
    for x in body:
        j = x
        for _ in range(1): #use 2 if u want rip 
            j = ast.Try(
                body=[random_match_case(),],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id=_memoryerror, ctx=ast.Load()),
                        name=rd(),
                        body=[j],
                    )
                ],
                orelse=[],
                finalbody=[],
            )
            j.body.append(
                ast.Raise(
                    exc=ast.Call(
                        func=ast.Name(id=_memoryerror, ctx=ast.Load()),
                        args=[],
                        keywords=[],
                    ),
                    cause=None,
                )
            )
        ar.append(j)
    return ar

class ReplaceIntegers(ast.NodeTransformer):
    def __init__(self):
        self.counter = 0 
        self.variables = {} 
    def visit_Num(self, node):
        if isinstance(node.n, int):
            new_var = f'{rd2()}'
            self.counter += 1
            self.variables[new_var] = node.n
            return ast.Name(id=new_var, ctx=ast.Load())
        return node

# class VariableToGlobalsTransformer(ast.NodeTransformer):
#     def visit_Name(self, node):
#         # Các loại Exception cần loại trừ
#         exception_types = {'Exception', 'MemoryError', 'ValueError', 'TypeError', 'IndexError', 'KeyError'}
        
#         # Chỉ xử lý các biến khi gắn giá trị (Store) và không phải Exception
#         if isinstance(node.ctx, ast.Store) and node.id not in exception_types:
#             return ast.Subscript(
#                 value=ast.Name(id='globals()', ctx=ast.Load()),
#                 slice=ast.Index(value=ast.Str(s=node.id)),
#                 ctx=node.ctx
#             )
# def globals_(source_code):
#     tree = ast.parse(source_code)
#     transformer = VariableToGlobalsTransformer()
#     transformed_tree = transformer.visit(tree)
#     return ast.unparse(transformed_tree)

def obf(code):
    def ps(x):
        return ast.parse(x)
    code = rename_function(ps(code),"print",__print)
    code = rename_function(ps(code),"input",__input)
    code = rename_function(ps(code),"__import__",___import__)
    code = rename_function(ps(code),"list",_list)
    #code = rename_function(ps(code),"str",_str)
    #code = rename_function(ps(code),"int",_int)
    code = rename_function(ps(code),"bytearray",_bytearray)
    code = rename_function(ps(code),"len",_len)
    tree = ps(code)
    obfuscate(tree)
    tbd = trycatch(tree.body, 1)
    def ast_to_code(node):
        return ast.unparse(node)
    
    j = ast_to_code(tbd)
    # j = globals_(j)
    return j



"""
 MODE 1 : LOW OBF (FOR ALL FILE) (EZ TO DEOBF)
 MODE 2 : MEDIUM (BEST CHOICE) (FULL STRING,INT,BOOL OBF)
 MODE 3 : HIGH (NOT RECOMMEND) (IT IS MEDIUM MODE BUT X2 SPAM)
 """


dark = Col.dark_gray
light = Col.light_gray
purple = Colors.StaticMIX((Col.purple, Col.red))
bpurple = Colors.StaticMIX((Col.pink, Col.blue, Col.blue))

text = f"""


    ┌─┐┬ ┬┌─┐┌─┐┬ ┬┌─┐┌─┐┬ ┬
    ├─┘└┬┘│ ┬├─┤│ ││ ┬├─┤│ │
────┴   ┴ └─┘┴ ┴└─┘└─┘┴ ┴└─┘

PLAN OBF (PREMIUM)


COPYRIGHT : TheSmartCat




"""

banner = f"""
"""






banner = Add.Add(text, banner, center=True)

print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, light)), banner))
def stage(text: str, symbol: str = 'PYGAUGAU PREMIUM V1', col1 = light, col2 = None) -> str:
    if col2 is None:
        col2 = light if symbol == 'PYGAUGAU PREMIUM V1' else purple
    return f""" {Col.Symbol(symbol, col1, dark)} {Colorate.Diagonal(Colors.DynamicMIX((Col.red, light)), text)}{light}"""

v = input
_v = print
def input(x):
    return v(stage(x))
def print(x,*k):
    return _v(stage(x),*k)
def ___print(x,*k):
    return _v(stage(x),*k,end='\r')
    



nhapuser = input(" NHẬP TÊN USER CỦA BẠN (ENTER YOUR NAME,EX : 'thesmartcat2303')) : ")
_file = input(" ENTER FILE: ")


import base64

def mh(t, k):
    return t,k

while True:
    try:

        with open(_file, "r", encoding="utf8") as file:
            code = file.read()
            code = "\n"+code
            code = code
            if _file == "bolangocuyencute.py":
                champ = mh(code,3)
            else:
                champ = " "

        break
    except FileNotFoundError:

        _file = input(" ENTER FILE AGAIN (file not found): ")
        

while True:
    try:
        #mode = int(input(" ENTER MODE: "))
        mode = 2
        if mode < 4:
            break
    except ValueError:
        pass

moreobf = input(" MORE OBF? (y/n): ")
antidebug = input(" CHỐNG SỬA ĐỔI BẢN QUYỀN , ANTI DEBUG (MAIN MODE) ? (y/n): ")
anticrack = input(" CHỐNG CRACK , ANTI CRACK REQUESTS LIB ? (y/n): ")
#method = input(" DO YOU WANT COMPILE? (y/n): ")
method = "y"
___print(" OBF LOADING... (30-600secs) ")

#code = ast.unparse(_moreobf(ast.parse(code)))
check = 0
code = _syntax(code)
if moreobf.upper() == "Y":
    code = __moreobf(code)
    check = 5
import os
import pystyle
requests_path = __import__('requests').__file__
_pystyle = pystyle.__file__
def caiditmemay(fl):
    tt = 0
    for root, dirs, files in os.walk(fl):
        for file in files:
            if file.endswith('.pyc'):
                continue
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    tt += len(content)
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")
    
    return tt


fl = os.path.dirname(__import__('requests').__file__)
tt = caiditmemay(fl)

_c = requests_path.replace('__init__.py','api.py')
_c1 = _pystyle
_x = open(_c,'r',encoding='utf8').read()
_x1 = open(_c1,'r',encoding='utf8').read()
_check = len(_x)
_check1 = len(_x1)
deptraia = r"""
list_func = ['print', 'open']
hooked_funcs = {}
inspect = __import__('inspect')
def hook_noi(func_name, *args, **kwargs):
    checked_paths = set()
    for frame in inspect.stack():
        filename = frame.filename
        if filename not in checked_paths:
            checked_paths.add(filename)
            try:
                module_names = ['requests', 'pystyle', 'ssl', 'socket', 'inspect', 'urllib']
                for module_name in module_names:
                    try:
                        if "requests" in module_name:
                            requests_path = __import__('os').path.dirname(__import__('os').path.abspath(__import__('requests').__file__))
                            api_path = __import__('os').path.join(requests_path, 'api.py')
                            if api_path in frame.filename:
                                try:__import__('sys').exit(f"Lỗi , Hãy Cài Lại Thư Viện Requests")
                                except:pass
                                finally:__import__('sys').exit(f"Lỗi , Hãy Cài Lại Thư Viện Requests")
                        module_path = __import__('os').path.abspath(__import__(module_name).__file__)
                        if module_path in filename:
                            try:__import__('sys').exit(f"Lỗi , Hãy Cài Lại Thư Viện {api_path}")
                            except:pass
                            finally:__import__('sys').exit(f"Lỗi , Hãy Cài Lại Thư Viện {api_path}")
                    except (ImportError, AttributeError,ModuleNotFoundError):
                        continue
            except Exception:
                pass
    hooked_funcs[func_name](*args, **kwargs)
def hook_check():
    for func_name in list_func:
        try:
            func = getattr(__builtins__, func_name)
            hooked_funcs[func_name] = func
            setattr(__builtins__, func_name, lambda *args, func_name=func_name, **kwargs: hook_noi(func_name, *args, **kwargs))
        except AttributeError:
            print(f"Warning: {{func_name}} not found in __builtins__")
def unhook():
    for func_name, original_func in hooked_funcs.items():
        setattr(__builtins__, func_name, original_func)
    hooked_funcs.clear()
hook_check()
import inspect
unhook()
"""
dz=  deptraia.encode()

rqprotect = f'''

exec({dz})

# '''


meh = """

from urllib.parse import urlparse
import _socket
from _socket import *
import os, sys, io, selectors
from enum import IntEnum, IntFlag
try:
    import errno
except ImportError:
    errno = None
EBADF = getattr(errno, 'EBADF', 9)
EAGAIN = getattr(errno, 'EAGAIN', 11)
EWOULDBLOCK = getattr(errno, 'EWOULDBLOCK', 11)

__all__ = ["fromfd", "getfqdn", "create_connection", "create_server",
           "has_dualstack_ipv6", "AddressFamily", "SocketKind"]
__all__.extend(os._get_exports_list(_socket))
IntEnum._convert_(
        'AddressFamily',
        __name__,
        lambda C: C.isupper() and C.startswith('AF_'))
IntEnum._convert_(
        'SocketKind',
        __name__,
        lambda C: C.isupper() and C.startswith('SOCK_'))
IntFlag._convert_(
        'MsgFlag',
        __name__,
        lambda C: C.isupper() and C.startswith('MSG_'))
IntFlag._convert_(
        'AddressInfo',
        __name__,
        lambda C: C.isupper() and C.startswith('AI_'))

_LOCALHOST    = '127.0.0.1'
_LOCALHOST_V6 = '::1'


def _intenum_converter(value, enum_klass):
    try:
        return enum_klass(value)
    except ValueError:
        return value
if sys.platform.lower().startswith("win"):
    errorTab = {}
    errorTab[6] = "Specified event object handle is invalid."
    errorTab[8] = "Insufficient memory available."
    errorTab[87] = "One or more parameters are invalid."
    errorTab[995] = "Overlapped operation aborted."
    errorTab[996] = "Overlapped I/O event object not in signaled state."
    errorTab[997] = "Overlapped operation will complete later."
    errorTab[10004] = "The operation was interrupted."
    errorTab[10009] = "A bad file handle was passed."
    errorTab[10013] = "Permission denied."
    errorTab[10014] = "A fault occurred on the network??"  # WSAEFAULT
    errorTab[10022] = "An invalid operation was attempted."
    errorTab[10024] = "Too many open files."
    errorTab[10035] = "The socket operation would block."
    errorTab[10036] = "A blocking operation is already in progress."
    errorTab[10037] = "Operation already in progress."
    errorTab[10038] = "Socket operation on nonsocket."
    errorTab[10039] = "Destination address required."
    errorTab[10040] = "Message too long."
    errorTab[10041] = "Protocol wrong type for socket."
    errorTab[10042] = "Bad protocol option."
    errorTab[10043] = "Protocol not supported."
    errorTab[10044] = "Socket type not supported."
    errorTab[10045] = "Operation not supported."
    errorTab[10046] = "Protocol family not supported."
    errorTab[10047] = "Address family not supported by protocol family."
    errorTab[10048] = "The network address is in use."
    errorTab[10049] = "Cannot assign requested address."
    errorTab[10050] = "Network is down."
    errorTab[10051] = "Network is unreachable."
    errorTab[10052] = "Network dropped connection on reset."
    errorTab[10053] = "Software caused connection abort."
    errorTab[10054] = "The connection has been reset."
    errorTab[10055] = "No buffer space available."
    errorTab[10056] = "Socket is already connected."
    errorTab[10057] = "Socket is not connected."
    errorTab[10058] = "The network has been shut down."
    errorTab[10059] = "Too many references."
    errorTab[10060] = "The operation timed out."
    errorTab[10061] = "Connection refused."
    errorTab[10062] = "Cannot translate name."
    errorTab[10063] = "The name is too long."
    errorTab[10064] = "The host is down."
    errorTab[10065] = "The host is unreachable."
    errorTab[10066] = "Directory not empty."
    errorTab[10067] = "Too many processes."
    errorTab[10068] = "User quota exceeded."
    errorTab[10069] = "Disk quota exceeded."
    errorTab[10070] = "Stale file handle reference."
    errorTab[10071] = "Item is remote."
    errorTab[10091] = "Network subsystem is unavailable."
    errorTab[10092] = "Winsock.dll version out of range."
    errorTab[10093] = "Successful WSAStartup not yet performed."
    errorTab[10101] = "Graceful shutdown in progress."
    errorTab[10102] = "No more results from WSALookupServiceNext."
    errorTab[10103] = "Call has been canceled."
    errorTab[10104] = "Procedure call table is invalid."
    errorTab[10105] = "Service provider is invalid."
    errorTab[10106] = "Service provider failed to initialize."
    errorTab[10107] = "System call failure."
    errorTab[10108] = "Service not found."
    errorTab[10109] = "Class type not found."
    errorTab[10110] = "No more results from WSALookupServiceNext."
    errorTab[10111] = "Call was canceled."
    errorTab[10112] = "Database query was refused."
    errorTab[11001] = "Host not found."
    errorTab[11002] = "Nonauthoritative host not found."
    errorTab[11003] = "This is a nonrecoverable error."
    errorTab[11004] = "Valid name, no data record requested type."
    errorTab[11005] = "QoS receivers."
    errorTab[11006] = "QoS senders."
    errorTab[11007] = "No QoS senders."
    errorTab[11008] = "QoS no receivers."
    errorTab[11009] = "QoS request confirmed."
    errorTab[11010] = "QoS admission error."
    errorTab[11011] = "QoS policy failure."
    errorTab[11012] = "QoS bad style."
    errorTab[11013] = "QoS bad object."
    errorTab[11014] = "QoS traffic control error."
    errorTab[11015] = "QoS generic error."
    errorTab[11016] = "QoS service type error."
    errorTab[11017] = "QoS flowspec error."
    errorTab[11018] = "Invalid QoS provider buffer."
    errorTab[11019] = "Invalid QoS filter style."
    errorTab[11020] = "Invalid QoS filter style."
    errorTab[11021] = "Incorrect QoS filter count."
    errorTab[11022] = "Invalid QoS object length."
    errorTab[11023] = "Incorrect QoS flow count."
    errorTab[11024] = "Unrecognized QoS object."
    errorTab[11025] = "Invalid QoS policy object."
    errorTab[11026] = "Invalid QoS flow descriptor."
    errorTab[11027] = "Invalid QoS provider-specific flowspec."
    errorTab[11028] = "Invalid QoS provider-specific filterspec."
    errorTab[11029] = "Invalid QoS shape discard mode object."
    errorTab[11030] = "Invalid QoS shaping rate object."
    errorTab[11031] = "Reserved policy QoS element type."
    __all__.append("errorTab")


class _GiveupOnSendfile(Exception): pass


class socket(_socket.socket):


    __slots__ = ["__weakref__", "_io_refs", "_closed"]

    def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
        if fileno is None:
            if family == -1:
                family = AF_INET
            if type == -1:
                type = SOCK_STREAM
            if proto == -1:
                proto = 0
        _socket.socket.__init__(self, family, type, proto, fileno)
        self._io_refs = 0
        self._closed = False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if not self._closed:
            self.close()

    def __repr__(self):
        closed = getattr(self, '_closed', False)
        s = "<%s.%s%s fd=%i, family=%s, type=%s, proto=%i" \
            % (self.__class__.__module__,
               self.__class__.__qualname__,
               " [closed]" if closed else "",
               self.fileno(),
               self.family,
               self.type,
               self.proto)
        if not closed:
            try:
                laddr = self.getsockname()
                if laddr:
                    s += ", laddr=%s" % str(laddr)
            except (error, AttributeError):
                pass
            try:
                raddr = self.getpeername()
                if raddr:
                    s += ", raddr=%s" % str(raddr)
            except (error, AttributeError):
                pass
        s += '>'
        return s

    def __getstate__(self):
        raise TypeError(f"cannot pickle {self.__class__.__name__!r} object")

    def dup(self):
        fd = dup(self.fileno())
        sock = self.__class__(self.family, self.type, self.proto, fileno=fd)
        sock.settimeout(self.gettimeout())
        return sock

    def accept(self):
        fd, addr = self._accept()
        sock = socket(self.family, self.type, self.proto, fileno=fd)
        # socket had a (non-zero) timeout, force the new socket in blocking
        if getdefaulttimeout() is None and self.gettimeout():
            sock.setblocking(True)
        return sock, addr

    def makefile(self, mode="r", buffering=None, *,
                 encoding=None, errors=None, newline=None):
        if not set(mode) <= {"r", "w", "b"}:
            raise ValueError("invalid mode %r (only r, w, b allowed)" % (mode,))
        writing = "w" in mode
        reading = "r" in mode or not writing
        assert reading or writing
        binary = "b" in mode
        rawmode = ""
        if reading:
            rawmode += "r"
        if writing:
            rawmode += "w"
        raw = SocketIO(self, rawmode)
        self._io_refs += 1
        if buffering is None:
            buffering = -1
        if buffering < 0:
            buffering = io.DEFAULT_BUFFER_SIZE
        if buffering == 0:
            if not binary:
                raise ValueError("unbuffered streams must be binary")
            return raw
        if reading and writing:
            buffer = io.BufferedRWPair(raw, raw, buffering)
        elif reading:
            buffer = io.BufferedReader(raw, buffering)
        else:
            assert writing
            buffer = io.BufferedWriter(raw, buffering)
        if binary:
            return buffer
        encoding = io.text_encoding(encoding)
        text = io.TextIOWrapper(buffer, encoding, errors, newline)
        text.mode = mode
        return text

    if hasattr(os, 'sendfile'):

        def _sendfile_use_sendfile(self, file, offset=0, count=None):
            self._check_sendfile_params(file, offset, count)
            sockno = self.fileno()
            try:
                fileno = file.fileno()
            except (AttributeError, io.UnsupportedOperation) as err:
                raise _GiveupOnSendfile(err)  
            try:
                fsize = os.fstat(fileno).st_size
            except OSError as err:
                raise _GiveupOnSendfile(err)  
            if not fsize:
                return 0  
            blocksize = min(count or fsize, 2 ** 30)
            timeout = self.gettimeout()
            if timeout == 0:
                raise ValueError("non-blocking sockets are not supported")
            # (also, they require a single syscall).
            if hasattr(selectors, 'PollSelector'):
                selector = selectors.PollSelector()
            else:
                selector = selectors.SelectSelector()
            selector.register(sockno, selectors.EVENT_WRITE)
            total_sent = 0
            selector_select = selector.select
            os_sendfile = os.sendfile
            try:
                while True:
                    if timeout and not selector_select(timeout):
                        raise TimeoutError('timed out')
                    if count:
                        blocksize = min(count - total_sent, blocksize)
                        if blocksize <= 0:
                            break
                    try:
                        sent = os_sendfile(sockno, fileno, offset, blocksize)
                    except BlockingIOError:
                        if not timeout:
                            selector_select()
                        continue
                    except OSError as err:
                        if total_sent == 0:
                            # one being 'file' is not a regular mmap(2)-like
                            # file, in which case we'll fall back on using
                            # plain send().
                            raise _GiveupOnSendfile(err)
                        raise err from None
                    else:
                        if sent == 0:
                            break  # EOF
                        offset += sent
                        total_sent += sent
                return total_sent
            finally:
                if total_sent > 0 and hasattr(file, 'seek'):
                    file.seek(offset)
    else:
        def _sendfile_use_sendfile(self, file, offset=0, count=None):
            raise _GiveupOnSendfile(
                "os.sendfile() not available on this platform")

    def _sendfile_use_send(self, file, offset=0, count=None):
        self._check_sendfile_params(file, offset, count)
        if self.gettimeout() == 0:
            raise ValueError("non-blocking sockets are not supported")
        if offset:
            file.seek(offset)
        blocksize = min(count, 8192) if count else 8192
        total_sent = 0
        # localize variable access to minimize overhead
        file_read = file.read
        sock_send = self.send
        try:
            while True:
                if count:
                    blocksize = min(count - total_sent, blocksize)
                    if blocksize <= 0:
                        break
                data = memoryview(file_read(blocksize))
                if not data:
                    break  # EOF
                while True:
                    try:
                        sent = sock_send(data)
                    except BlockingIOError:
                        continue
                    else:
                        total_sent += sent
                        if sent < len(data):
                            data = data[sent:]
                        else:
                            break
            return total_sent
        finally:
            if total_sent > 0 and hasattr(file, 'seek'):
                file.seek(offset + total_sent)

    def _check_sendfile_params(self, file, offset, count):
        if 'b' not in getattr(file, 'mode', 'b'):
            raise ValueError("file should be opened in binary mode")
        if not self.type & SOCK_STREAM:
            raise ValueError("only SOCK_STREAM type sockets are supported")
        if count is not None:
            if not isinstance(count, int):
                raise TypeError(
                    "count must be a positive integer (got {!r})".format(count))
            if count <= 0:
                raise ValueError(
                    "count must be a positive integer (got {!r})".format(count))

    def sendfile(self, file, offset=0, count=None):
        try:
            return self._sendfile_use_sendfile(file, offset, count)
        except _GiveupOnSendfile:
            return self._sendfile_use_send(file, offset, count)

    def _decref_socketios(self):
        if self._io_refs > 0:
            self._io_refs -= 1
        if self._closed:
            self.close()

    def _real_close(self, _ss=_socket.socket):
        _ss.close(self)

    def close(self):
        self._closed = True
        if self._io_refs <= 0:
            self._real_close()

    def detach(self):
        self._closed = True
        return super().detach()

    @property
    def family(self):
        return _intenum_converter(super().family, AddressFamily)

    @property
    def type(self):
        return _intenum_converter(super().type, SocketKind)

    if os.name == 'nt':
        def get_inheritable(self):
            return os.get_handle_inheritable(self.fileno())
        def set_inheritable(self, inheritable):
            os.set_handle_inheritable(self.fileno(), inheritable)
    else:
        def get_inheritable(self):
            return os.get_inheritable(self.fileno())
        def set_inheritable(self, inheritable):
            os.set_inheritable(self.fileno(), inheritable)
    get_inheritable.__doc__ = "Get the inheritable flag of the socket"
    set_inheritable.__doc__ = "Set the inheritable flag of the socket"

def fromfd(fd, family, type, proto=0):
    nfd = dup(fd)
    return socket(family, type, proto, nfd)
if hasattr(_socket.socket, "sendmsg"):
    import array

    def send_fds(sock, buffers, fds, flags=0, address=None):

        return sock.sendmsg(buffers, [(_socket.SOL_SOCKET,
            _socket.SCM_RIGHTS, array.array("i", fds))])
    __all__.append("send_fds")

if hasattr(_socket.socket, "recvmsg"):
    import array

    def recv_fds(sock, bufsize, maxfds, flags=0):

        # Array of ints
        fds = array.array("i")
        msg, ancdata, flags, addr = sock.recvmsg(bufsize,
            _socket.CMSG_LEN(maxfds * fds.itemsize))
        for cmsg_level, cmsg_type, cmsg_data in ancdata:
            if (cmsg_level == _socket.SOL_SOCKET and cmsg_type == _socket.SCM_RIGHTS):
                fds.frombytes(cmsg_data[:
                        len(cmsg_data) - (len(cmsg_data) % fds.itemsize)])

        return msg, list(fds), flags, addr
    __all__.append("recv_fds")

if hasattr(_socket.socket, "share"):
    def fromshare(info):

        return socket(0, 0, 0, info)
    __all__.append("fromshare")

if hasattr(_socket, "socketpair"):
    def socketpair(family=None, type=SOCK_STREAM, proto=0):
        if family is None:
            try:
                family = AF_UNIX
            except NameError:
                family = AF_INET
        a, b = _socket.socketpair(family, type, proto)
        a = socket(family, type, proto, a.detach())
        b = socket(family, type, proto, b.detach())
        return a, b
else:
    def socketpair(family=AF_INET, type=SOCK_STREAM, proto=0):
        if family == AF_INET:
            host = _LOCALHOST
        elif family == AF_INET6:
            host = _LOCALHOST_V6
        else:
            raise ValueError("Only AF_INET and AF_INET6 socket address families "
                             "are supported")
        if type != SOCK_STREAM:
            raise ValueError("Only SOCK_STREAM socket type is supported")
        if proto != 0:
            raise ValueError("Only protocol zero is supported")
        lsock = socket(family, type, proto)
        try:
            lsock.bind((host, 0))
            lsock.listen()
            # On IPv6, ignore flow_info and scope_id
            addr, port = lsock.getsockname()[:2]
            csock = socket(family, type, proto)
            try:
                csock.setblocking(False)
                try:
                    csock.connect((addr, port))
                except (BlockingIOError, InterruptedError):
                    pass
                csock.setblocking(True)
                ssock, _ = lsock.accept()
            except:
                csock.close()
                raise
        finally:
            lsock.close()
        return (ssock, csock)
    __all__.append("socketpair")

_blocking_errnos = { EAGAIN, EWOULDBLOCK }

class SocketIO(io.RawIOBase):


    def __init__(self, sock, mode):
        if mode not in ("r", "w", "rw", "rb", "wb", "rwb"):
            raise ValueError("invalid mode: %r" % mode)
        io.RawIOBase.__init__(self)
        self._sock = sock
        if "b" not in mode:
            mode += "b"
        self._mode = mode
        self._reading = "r" in mode
        self._writing = "w" in mode
        self._timeout_occurred = False

    def readinto(self, b):
        self._checkClosed()
        self._checkReadable()
        if self._timeout_occurred:
            raise OSError("cannot read from timed out object")
        while True:
            try:
                return self._sock.recv_into(b)
            except timeout:
                self._timeout_occurred = True
                raise
            except error as e:
                if e.errno in _blocking_errnos:
                    return None
                raise

    def write(self, b):
        self._checkClosed()
        self._checkWritable()
        try:
            return self._sock.send(b)
        except error as e:
            if e.errno in _blocking_errnos:
                return None
            raise

    def readable(self):
        if self.closed:
            raise ValueError("I/O operation on closed socket.")
        return self._reading

    def writable(self):
        if self.closed:
            raise ValueError("I/O operation on closed socket.")
        return self._writing

    def seekable(self):
        if self.closed:
            raise ValueError("I/O operation on closed socket.")
        return super().seekable()

    def fileno(self):
        self._checkClosed()
        return self._sock.fileno()

    @property
    def name(self):
        if not self.closed:
            return self.fileno()
        else:
            return -1

    @property
    def mode(self):
        return self._mode

    def close(self):

        if self.closed:
            return
        io.RawIOBase.close(self)
        self._sock._decref_socketios()
        self._sock = None


def getfqdn(name=''):
    name = name.strip()
    if not name or name in ('0.0.0.0', '::'):
        name = gethostname()
    try:
        hostname, aliases, ipaddrs = gethostbyaddr(name)
    except error:
        pass
    else:
        aliases.insert(0, hostname)
        for name in aliases:
            if '.' in name:
                break
        else:
            name = hostname
    return name
_GLOBAL_DEFAULT_TIMEOUT = object()
def create_connection(address, timeout=_GLOBAL_DEFAULT_TIMEOUT,
                      source_address=None, *, all_errors=False):
    host, port = address
    exceptions = []
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        sock = None
        try:
            sock = socket(af, socktype, proto)
            if timeout is not _GLOBAL_DEFAULT_TIMEOUT:
                sock.settimeout(timeout)
            if source_address:
                sock.bind(source_address)
            sock.connect(sa)
            exceptions.clear()
            return sock

        except error as exc:
            if not all_errors:
                exceptions.clear()  # raise only the last error
            exceptions.append(exc)
            if sock is not None:
                sock.close()

    if len(exceptions):
        try:
            if not all_errors:
                raise exceptions[0]
            raise ExceptionGroup("create_connection failed", exceptions)
        finally:
            exceptions.clear()
    else:
        raise error("getaddrinfo returns an empty list")
def has_dualstack_ipv6():
    if not has_ipv6 \
            or not hasattr(_socket, 'IPPROTO_IPV6') \
            or not hasattr(_socket, 'IPV6_V6ONLY'):
        return False
    try:
        with socket(AF_INET6, SOCK_STREAM) as sock:
            sock.setsockopt(IPPROTO_IPV6, IPV6_V6ONLY, 0)
            return True
    except error:
        return False
def create_server(address, *, family=AF_INET, backlog=None, reuse_port=False,
                  dualstack_ipv6=False):
    if reuse_port and not hasattr(_socket, "SO_REUSEPORT"):
        raise ValueError("SO_REUSEPORT not supported on this platform")
    if dualstack_ipv6:
        if not has_dualstack_ipv6():
            raise ValueError("dualstack_ipv6 not supported on this platform")
        if family != AF_INET6:
            raise ValueError("dualstack_ipv6 requires AF_INET6 family")
    sock = socket(family, SOCK_STREAM)
    try:
        if os.name not in ('nt', 'cygwin') and \
                hasattr(_socket, 'SO_REUSEADDR'):
            try:
                sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            except error:
                pass
        if reuse_port:
            sock.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
        if has_ipv6 and family == AF_INET6:
            if dualstack_ipv6:
                sock.setsockopt(IPPROTO_IPV6, IPV6_V6ONLY, 0)
            elif hasattr(_socket, "IPV6_V6ONLY") and \
                    hasattr(_socket, "IPPROTO_IPV6"):
                sock.setsockopt(IPPROTO_IPV6, IPV6_V6ONLY, 1)
        try:
            sock.bind(address)
        except error as err:
            msg = '%s (while attempting to bind on address %r)' % \
                (err.strerror, address)
            raise error(err.errno, msg) from None
        if backlog is None:
            sock.listen()
        else:
            sock.listen(backlog)
        return sock
    except error:
        sock.close()
        raise
def getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
    addrlist = []
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
        af, socktype, proto, canonname, sa = res
        addrlist.appen
"""
meh = ''

rqprotect1 = r"""
from requests.status_codes import codes
from urllib.parse import urljoin, urlparse
from requests._internal_utils import to_native_string
from requests.cookies import extract_cookies_to_jar, merge_cookies
from requests.exceptions import ChunkedEncodingError, ContentDecodingError, TooManyRedirects
from requests.utils import DEFAULT_PORTS, get_auth_from_url, get_environ_proxies, get_netrc_auth, requote_uri, rewind_body, should_bypass_proxies
import os
import sys
import time
from collections import OrderedDict
from datetime import timedelta
from requests.adapters import HTTPAdapter
from requests.compat import Mapping, cookielib, urljoin, urlparse
from requests.cookies import RequestsCookieJar, cookiejar_from_dict, extract_cookies_to_jar, merge_cookies
from requests.exceptions import ChunkedEncodingError, ContentDecodingError, InvalidSchema, TooManyRedirects
from requests.hooks import default_hooks, dispatch_hook
from requests.models import DEFAULT_REDIRECT_LIMIT, REDIRECT_STATI, PreparedRequest, Request
from requests.utils import DEFAULT_PORTS, default_headers, get_auth_from_url, get_environ_proxies, get_netrc_auth, requote_uri, resolve_proxies, rewind_body, should_bypass_proxies, to_key_val_list
import os.path
import socket
import typing
import warnings
from urllib3.exceptions import ClosedPoolError, ConnectTimeoutError
from urllib3.exceptions import HTTPError as _HTTPError
from urllib3.exceptions import InvalidHeader as _InvalidHeader
from urllib3.exceptions import LocationValueError, MaxRetryError, NewConnectionError, ProtocolError
from urllib3.exceptions import ProxyError as _ProxyError
from urllib3.exceptions import ReadTimeoutError, ResponseError
from urllib3.exceptions import SSLError as _SSLError
from urllib3.poolmanager import PoolManager, proxy_from_url
from urllib3.util import Timeout as TimeoutSauce
from urllib3.util import parse_url
from urllib3.util.retry import Retry
from requests.auth import _basic_auth_str
from requests.compat import basestring, urlparse
from requests.cookies import extract_cookies_to_jar
from requests.exceptions import ConnectionError, ConnectTimeout, InvalidHeader, InvalidProxyURL, InvalidSchema, InvalidURL, ProxyError, ReadTimeout, RetryError, SSLError
from requests.models import Response
from requests.utils import DEFAULT_CA_BUNDLE_PATH, extract_zipped_paths, get_auth_from_url, get_encoding_from_headers, prepend_scheme_if_needed, select_proxy, urldefragauth
try:
    from urllib3.contrib.socks import SOCKSProxyManager
except ImportError:

    def SOCKSProxyManager(*args, **kwargs):
        raise InvalidSchema('Missing dependencies for SOCKS support.')
if typing.TYPE_CHECKING:
    from requests.models import PreparedRequest
DEFAULT_POOLBLOCK = False
DEFAULT_POOLSIZE = 10
DEFAULT_RETRIES = 0
DEFAULT_POOL_TIMEOUT = None

def _urllib3_request_context(request: 'PreparedRequest', verify: 'bool | str | None', client_cert: 'typing.Tuple[str, str] | str | None', poolmanager: 'PoolManager') -> '(typing.Dict[str, typing.Any], typing.Dict[str, typing.Any])':
    host_params = {}
    pool_kwargs = {}
    parsed_request_url = urlparse(request.url)
    scheme = parsed_request_url.scheme.lower()
    port = parsed_request_url.port
    cert_reqs = 'CERT_REQUIRED'
    if verify is False:
        cert_reqs = 'CERT_NONE'
    elif isinstance(verify, str):
        if not os.path.isdir(verify):
            pool_kwargs['ca_certs'] = verify
        else:
            pool_kwargs['ca_cert_dir'] = verify
    pool_kwargs['cert_reqs'] = cert_reqs
    if client_cert is not None:
        if isinstance(client_cert, tuple) and len(client_cert) == 2:
            pool_kwargs['cert_file'] = client_cert[0]
            pool_kwargs['key_file'] = client_cert[1]
        else:
            pool_kwargs['cert_file'] = client_cert
    host_params = {'scheme': scheme, 'host': parsed_request_url.hostname, 'port': port}
    return (host_params, pool_kwargs)

class BaseAdapter:

    def __init__(self):
        super().__init__()

    def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

class HTTPAdapter(BaseAdapter):
    __attrs__ = ['max_retries', 'config', '_pool_connections', '_pool_maxsize', '_pool_block']

    def __init__(self, pool_connections=DEFAULT_POOLSIZE, pool_maxsize=DEFAULT_POOLSIZE, max_retries=DEFAULT_RETRIES, pool_block=DEFAULT_POOLBLOCK):
        if max_retries == DEFAULT_RETRIES:
            self.max_retries = Retry(0, read=False)
        else:
            self.max_retries = Retry.from_int(max_retries)
        self.config = {}
        self.proxy_manager = {}
        super().__init__()
        self._pool_connections = pool_connections
        self._pool_maxsize = pool_maxsize
        self._pool_block = pool_block
        self.init_poolmanager(pool_connections, pool_maxsize, block=pool_block)

    def __getstate__(self):
        return {attr: getattr(self, attr, None) for attr in self.__attrs__}

    def __setstate__(self, state):
        self.proxy_manager = {}
        self.config = {}
        for attr, value in state.items():
            setattr(self, attr, value)
        self.init_poolmanager(self._pool_connections, self._pool_maxsize, block=self._pool_block)

    def init_poolmanager(self, connections, maxsize, block=DEFAULT_POOLBLOCK, **pool_kwargs):
        self._pool_connections = connections
        self._pool_maxsize = maxsize
        self._pool_block = block
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block, **pool_kwargs)

    def proxy_manager_for(self, proxy, **proxy_kwargs):
        if proxy in self.proxy_manager:
            manager = self.proxy_manager[proxy]
        elif proxy.lower().startswith('socks'):
            username, password = get_auth_from_url(proxy)
            manager = self.proxy_manager[proxy] = SOCKSProxyManager(proxy, username=username, password=password, num_pools=self._pool_connections, maxsize=self._pool_maxsize, block=self._pool_block, **proxy_kwargs)
        else:
            proxy_headers = self.proxy_headers(proxy)
            manager = self.proxy_manager[proxy] = proxy_from_url(proxy, proxy_headers=proxy_headers, num_pools=self._pool_connections, maxsize=self._pool_maxsize, block=self._pool_block, **proxy_kwargs)
        return manager

    def cert_verify(self, conn, url, verify, cert):
        if url.lower().startswith('https') and verify:
            cert_loc = None
            if verify is not True:
                cert_loc = verify
            if not cert_loc:
                cert_loc = extract_zipped_paths(DEFAULT_CA_BUNDLE_PATH)
            if not cert_loc or not os.path.exists(cert_loc):
                raise OSError(f'Could not find a suitable TLS CA certificate bundle, invalid path: {cert_loc}')
            conn.cert_reqs = 'CERT_REQUIRED'
            if not os.path.isdir(cert_loc):
                conn.ca_certs = cert_loc
            else:
                conn.ca_cert_dir = cert_loc
        else:
            conn.cert_reqs = 'CERT_NONE'
            conn.ca_certs = None
            conn.ca_cert_dir = None
        if cert:
            if not isinstance(cert, basestring):
                conn.cert_file = cert[0]
                conn.key_file = cert[1]
            else:
                conn.cert_file = cert
                conn.key_file = None
            if conn.cert_file and (not os.path.exists(conn.cert_file)):
                raise OSError(f'Could not find the TLS certificate file, invalid path: {conn.cert_file}')
            if conn.key_file and (not os.path.exists(conn.key_file)):
                raise OSError(f'Could not find the TLS key file, invalid path: {conn.key_file}')

    def build_response(self, req, resp):
        response = Response()
        response.status_code = getattr(resp, 'status', None)
        response.headers = CaseInsensitiveDict(getattr(resp, 'headers', {}))
        response.encoding = get_encoding_from_headers(response.headers)
        response.raw = resp
        response.reason = response.raw.reason
        if isinstance(req.url, bytes):
            response.url = req.url.decode('utf-8')
        else:
            response.url = req.url
        extract_cookies_to_jar(response.cookies, req, resp)
        response.request = req
        response.connection = self
        return response

    def build_connection_pool_key_attributes(self, request, verify, cert=None):
        return _urllib3_request_context(request, verify, cert, self.poolmanager)

    def get_connection_with_tls_context(self, request, verify, proxies=None, cert=None):
        proxy = select_proxy(request.url, proxies)
        try:
            host_params, pool_kwargs = self.build_connection_pool_key_attributes(request, verify, cert)
        except ValueError as e:
            raise InvalidURL(e, request=request)
        if proxy:
            proxy = prepend_scheme_if_needed(proxy, 'http')
            proxy_url = parse_url(proxy)
            if not proxy_url.host:
                raise InvalidProxyURL('Please check proxy URL. It is malformed and could be missing the host.')
            proxy_manager = self.proxy_manager_for(proxy)
            conn = proxy_manager.connection_from_host(**host_params, pool_kwargs=pool_kwargs)
        else:
            conn = self.poolmanager.connection_from_host(**host_params, pool_kwargs=pool_kwargs)
        return conn

    def get_connection(self, url, proxies=None):
        warnings.warn('`get_connection` has been deprecated in favor of `get_connection_with_tls_context`. Custom HTTPAdapter subclasses will need to migrate for Requests>=2.32.2. Please see https://github.com/psf/requests/pull/6710 for more details.', DeprecationWarning)
        proxy = select_proxy(url, proxies)
        if proxy:
            proxy = prepend_scheme_if_needed(proxy, 'http')
            proxy_url = parse_url(proxy)
            if not proxy_url.host:
                raise InvalidProxyURL('Please check proxy URL. It is malformed and could be missing the host.')
            proxy_manager = self.proxy_manager_for(proxy)
            conn = proxy_manager.connection_from_url(url)
        else:
            parsed = urlparse(url)
            url = parsed.geturl()
            conn = self.poolmanager.connection_from_url(url)
        return conn

    def close(self):
        self.poolmanager.clear()
        for proxy in self.proxy_manager.values():
            proxy.clear()

    def request_url(self, request, proxies):
        proxy = select_proxy(request.url, proxies)
        scheme = urlparse(request.url).scheme
        is_proxied_http_request = proxy and scheme != 'https'
        using_socks_proxy = False
        if proxy:
            proxy_scheme = urlparse(proxy).scheme.lower()
            using_socks_proxy = proxy_scheme.startswith('socks')
        url = request.path_url
        if url.startswith('//'):
            url = f'/{url.lstrip('/')}'
        if is_proxied_http_request and (not using_socks_proxy):
            url = urldefragauth(request.url)
        return url

    def add_headers(self, request, **kwargs):
        pass

    def proxy_headers(self, proxy):
        headers = {}
        username, password = get_auth_from_url(proxy)
        if username:
            headers['Proxy-Authorization'] = _basic_auth_str(username, password)
        return headers

    def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        try:
            conn = self.get_connection_with_tls_context(request, verify, proxies=proxies, cert=cert)
        except LocationValueError as e:
            raise InvalidURL(e, request=request)
        self.cert_verify(conn, request.url, verify, cert)
        url = self.request_url(request, proxies)
        self.add_headers(request, stream=stream, timeout=timeout, verify=verify, cert=cert, proxies=proxies)
        chunked = not (request.body is None or 'Content-Length' in request.headers)
        if isinstance(timeout, tuple):
            try:
                connect, read = timeout
                timeout = TimeoutSauce(connect=connect, read=read)
            except ValueError:
                raise ValueError(f'Invalid timeout {timeout}. Pass a (connect, read) timeout tuple, or a single float to set both timeouts to the same value.')
        elif isinstance(timeout, TimeoutSauce):
            pass
        else:
            timeout = TimeoutSauce(connect=timeout, read=timeout)
        try:
            resp = conn.urlopen(method=request.method, url=url, body=request.body, headers=request.headers, redirect=False, assert_same_host=False, preload_content=False, decode_content=False, retries=self.max_retries, timeout=timeout, chunked=chunked)
        except (ProtocolError, OSError) as err:
            raise ConnectionError(err, request=request)
        except MaxRetryError as e:
            if isinstance(e.reason, ConnectTimeoutError):
                if not isinstance(e.reason, NewConnectionError):
                    raise ConnectTimeout(e, request=request)
            if isinstance(e.reason, ResponseError):
                raise RetryError(e, request=request)
            if isinstance(e.reason, _ProxyError):
                raise ProxyError(e, request=request)
            if isinstance(e.reason, _SSLError):
                raise SSLError(e, request=request)
            raise ConnectionError(e, request=request)
        except ClosedPoolError as e:
            raise ConnectionError(e, request=request)
        except _ProxyError as e:
            raise ProxyError(e)
        except (_SSLError, _HTTPError) as e:
            if isinstance(e, _SSLError):
                raise SSLError(e, request=request)
            elif isinstance(e, ReadTimeoutError):
                raise ReadTimeout(e, request=request)
            elif isinstance(e, _InvalidHeader):
                raise InvalidHeader(e, request=request)
            else:
                raise
        return self.build_response(request, resp)
if sys.platform == 'win32':
    preferred_clock = time.perf_counter
else:
    preferred_clock = time.time

def merge_setting(request_setting, session_setting, dict_class=OrderedDict):
    if session_setting is None:
        return request_setting
    if request_setting is None:
        return session_setting
    if not (isinstance(session_setting, Mapping) and isinstance(request_setting, Mapping)):
        return request_setting
    merged_setting = dict_class(to_key_val_list(session_setting))
    merged_setting.update(to_key_val_list(request_setting))
    none_keys = [k for k, v in merged_setting.items() if v is None]
    for key in none_keys:
        del merged_setting[key]
    return merged_setting

def merge_hooks(request_hooks, session_hooks, dict_class=OrderedDict):
    if session_hooks is None or session_hooks.get('response') == []:
        return request_hooks
    if request_hooks is None or request_hooks.get('response') == []:
        return session_hooks
    return merge_setting(request_hooks, session_hooks, dict_class)

class SessionRedirectMixin:

    def get_redirect_target(self, resp):
        if resp.is_redirect:
            location = resp.headers['location']
            location = location.encode('latin1')
            return to_native_string(location, 'utf8')
        return None

    def should_strip_auth(self, old_url, new_url):
        old_parsed = urlparse(old_url)
        new_parsed = urlparse(new_url)
        if old_parsed.hostname != new_parsed.hostname:
            return True
        if old_parsed.scheme == 'http' and old_parsed.port in (80, None) and (new_parsed.scheme == 'https') and (new_parsed.port in (443, None)):
            return False
        changed_port = old_parsed.port != new_parsed.port
        changed_scheme = old_parsed.scheme != new_parsed.scheme
        default_port = (DEFAULT_PORTS.get(old_parsed.scheme, None), None)
        if not changed_scheme and old_parsed.port in default_port and (new_parsed.port in default_port):
            return False
        return changed_port or changed_scheme

    def resolve_redirects(self, resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs):
        hist = []
        url = self.get_redirect_target(resp)
        previous_fragment = urlparse(req.url).fragment
        while url:
            prepared_request = req.copy()
            hist.append(resp)
            resp.history = hist[1:]
            try:
                resp.content
            except (ChunkedEncodingError, ContentDecodingError, RuntimeError):
                resp.raw.read(decode_content=False)
            if len(resp.history) >= self.max_redirects:
                raise TooManyRedirects(f'Exceeded {self.max_redirects} redirects.', response=resp)
            resp.close()
            if url.startswith('//'):
                parsed_rurl = urlparse(resp.url)
                url = ':'.join([to_native_string(parsed_rurl.scheme), url])
            parsed = urlparse(url)
            if parsed.fragment == '' and previous_fragment:
                parsed = parsed._replace(fragment=previous_fragment)
            elif parsed.fragment:
                previous_fragment = parsed.fragment
            url = parsed.geturl()
            if not parsed.netloc:
                url = urljoin(resp.url, requote_uri(url))
            else:
                url = requote_uri(url)
            prepared_request.url = to_native_string(url)
            self.rebuild_method(prepared_request, resp)
            if resp.status_code not in (codes.temporary_redirect, codes.permanent_redirect):
                purged_headers = ('Content-Length', 'Content-Type', 'Transfer-Encoding')
                for header in purged_headers:
                    prepared_request.headers.pop(header, None)
                prepared_request.body = None
            headers = prepared_request.headers
            headers.pop('Cookie', None)
            extract_cookies_to_jar(prepared_request._cookies, req, resp.raw)
            merge_cookies(prepared_request._cookies, self.cookies)
            prepared_request.prepare_cookies(prepared_request._cookies)
            proxies = self.rebuild_proxies(prepared_request, proxies)
            self.rebuild_auth(prepared_request, resp)
            rewindable = prepared_request._body_position is not None and ('Content-Length' in headers or 'Transfer-Encoding' in headers)
            if rewindable:
                rewind_body(prepared_request)
            req = prepared_request
            if yield_requests:
                yield req
            else:
                resp = self.send(req, stream=stream, timeout=timeout, verify=verify, cert=cert, proxies=proxies, allow_redirects=False, **adapter_kwargs)
                extract_cookies_to_jar(self.cookies, prepared_request, resp.raw)
                url = self.get_redirect_target(resp)
                yield resp

    def rebuild_auth(self, prepared_request, response):
        headers = prepared_request.headers
        url = prepared_request.url
        if 'Authorization' in headers and self.should_strip_auth(response.request.url, url):
            del headers['Authorization']
        new_auth = get_netrc_auth(url) if self.trust_env else None
        if new_auth is not None:
            prepared_request.prepare_auth(new_auth)

    def rebuild_proxies(self, prepared_request, proxies):
        headers = prepared_request.headers
        scheme = urlparse(prepared_request.url).scheme
        new_proxies = resolve_proxies(prepared_request, proxies, self.trust_env)
        if 'Proxy-Authorization' in headers:
            del headers['Proxy-Authorization']
        try:
            username, password = get_auth_from_url(new_proxies[scheme])
        except KeyError:
            username, password = (None, None)
        if not scheme.startswith('https') and username and password:
            headers['Proxy-Authorization'] = _basic_auth_str(username, password)
        return new_proxies

    def rebuild_method(self, prepared_request, response):
        method = prepared_request.method
        if response.status_code == codes.see_other and method != 'HEAD':
            method = 'GET'
        if response.status_code == codes.found and method != 'HEAD':
            method = 'GET'
        if response.status_code == codes.moved and method == 'POST':
            method = 'GET'
        prepared_request.method = method

class Session(SessionRedirectMixin):
    __attrs__ = ['headers', 'cookies', 'auth', 'proxies', 'hooks', 'params', 'verify', 'cert', 'adapters', 'stream', 'trust_env', 'max_redirects']

    def __init__(self):
        self.headers = default_headers()
        self.auth = None
        self.proxies = {}
        self.hooks = default_hooks()
        self.params = {}
        self.stream = False
        self.verify = True
        self.cert = None
        self.max_redirects = DEFAULT_REDIRECT_LIMIT
        self.trust_env = True
        self.cookies = cookiejar_from_dict({})
        self.adapters = OrderedDict()
        self.mount('https://', HTTPAdapter())
        self.mount('http://', HTTPAdapter())

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def prepare_request(self, request):
        cookies = request.cookies or {}
        if not isinstance(cookies, cookielib.CookieJar):
            cookies = cookiejar_from_dict(cookies)
        merged_cookies = merge_cookies(merge_cookies(RequestsCookieJar(), self.cookies), cookies)
        auth = request.auth
        if self.trust_env and (not auth) and (not self.auth):
            auth = get_netrc_auth(request.url)
        p = PreparedRequest()
        p.prepare(method=request.method.upper(), url=request.url, files=request.files, data=request.data, json=request.json, headers=merge_setting(request.headers, self.headers, dict_class=CaseInsensitiveDict), params=merge_setting(request.params, self.params), auth=merge_setting(auth, self.auth), cookies=merged_cookies, hooks=merge_hooks(request.hooks, self.hooks))
        return p

    def request(self, method, url, params=None, data=None, headers=None, cookies=None, files=None, auth=None, timeout=None, allow_redirects=True, proxies=None, hooks=None, stream=None, verify=None, cert=None, json=None):
        req = Request(method=method.upper(), url=url, headers=headers, files=files, data=data or {}, json=json, params=params or {}, auth=auth, cookies=cookies, hooks=hooks)
        prep = self.prepare_request(req)
        proxies = proxies or {}
        settings = self.merge_environment_settings(prep.url, proxies, stream, verify, cert)
        send_kwargs = {'timeout': timeout, 'allow_redirects': allow_redirects}
        send_kwargs.update(settings)
        resp = self.send(prep, **send_kwargs)
        return resp

    def get(self, url, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return self.request('GET', url, **kwargs)

    def options(self, url, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return self.request('OPTIONS', url, **kwargs)

    def head(self, url, **kwargs):
        kwargs.setdefault('allow_redirects', False)
        return self.request('HEAD', url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request('POST', url, data=data, json=json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request('PUT', url, data=data, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request('PATCH', url, data=data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)

    def send(self, request, **kwargs):
        kwargs.setdefault('stream', self.stream)
        kwargs.setdefault('verify', self.verify)
        kwargs.setdefault('cert', self.cert)
        if 'proxies' not in kwargs:
            kwargs['proxies'] = resolve_proxies(request, self.proxies, self.trust_env)
        if isinstance(request, Request):
            raise ValueError('You can only send PreparedRequests.')
        allow_redirects = kwargs.pop('allow_redirects', True)
        stream = kwargs.get('stream')
        hooks = request.hooks
        adapter = self.get_adapter(url=request.url)
        start = preferred_clock()
        r = adapter.send(request, **kwargs)
        elapsed = preferred_clock() - start
        r.elapsed = timedelta(seconds=elapsed)
        r = dispatch_hook('response', hooks, r, **kwargs)
        if r.history:
            for resp in r.history:
                extract_cookies_to_jar(self.cookies, resp.request, resp.raw)
        extract_cookies_to_jar(self.cookies, request, r.raw)
        if allow_redirects:
            gen = self.resolve_redirects(r, request, **kwargs)
            history = [resp for resp in gen]
        else:
            history = []
        if history:
            history.insert(0, r)
            r = history.pop()
            r.history = history
        if not allow_redirects:
            try:
                r._next = next(self.resolve_redirects(r, request, yield_requests=True, **kwargs))
            except StopIteration:
                pass
        if not stream:
            r.content
        return r

    def merge_environment_settings(self, url, proxies, stream, verify, cert):
        if self.trust_env:
            no_proxy = proxies.get('no_proxy') if proxies is not None else None
            env_proxies = get_environ_proxies(url, no_proxy=no_proxy)
            for k, v in env_proxies.items():
                proxies.setdefault(k, v)
            if verify is True or verify is None:
                verify = os.environ.get('REQUESTS_CA_BUNDLE') or os.environ.get('CURL_CA_BUNDLE') or verify
        proxies = merge_setting(proxies, self.proxies)
        stream = merge_setting(stream, self.stream)
        verify = merge_setting(verify, self.verify)
        cert = merge_setting(cert, self.cert)
        return {'proxies': proxies, 'stream': stream, 'verify': verify, 'cert': cert}

    def get_adapter(self, url):
        for prefix, adapter in self.adapters.items():
            if url.lower().startswith(prefix.lower()):
                return adapter
        raise InvalidSchema(f'No connection adapters were found for {url!r}')

    def close(self):
        for v in self.adapters.values():
            v.close()

    def mount(self, prefix, adapter):
        self.adapters[prefix] = adapter
        keys_to_move = [k for k in self.adapters if len(k) < len(prefix)]
        for key in keys_to_move:
            self.adapters[key] = self.adapters.pop(key)

    def __getstate__(self):
        state = {attr: getattr(self, attr, None) for attr in self.__attrs__}
        return state

    def __setstate__(self, state):
        for attr, value in state.items():
            setattr(self, attr, value)

def session():
    return Session()
class Session:
    def __init__(self):
        self.headers = __import__('requests').structures.CaseInsensitiveDict({
        'User-Agent': 'python-requests/2.31.0',
        'Accept-Encoding': ', '.join(('gzip', 'deflate')),
        'Accept': '*/*',
        'Connection': 'keep-alive',
    })
        self.auth = None
        self.proxies = {}
        self.hooks = {event: [] for event in ['response']}
        self.params = {}
        self.stream = False
        self.verify = True
        self.cert = None
        self.max_redirects = 30
        self.trust_env = True
        self.cookies = __import__('requests').cookies.cookiejar_from_dict({})
        self.adapters = __import__('collections').OrderedDict()
        self.HTTPAdapter = __import__('requests').adapters.HTTPAdapter()
        if __import__('sys').platform == 'win32':
            try:self.preferred_clock = __import__('time').perf_counter
            except AttributeError:self.preferred_clock = __import__('time').clock
        else:self.preferred_clock = __import__('time').time
        self.mount('https://', self.HTTPAdapter)
        self.mount('http://', self.HTTPAdapter)
    def get_redirect_target(self, resp):
        if resp.is_redirect:
            location = resp.headers['location']
            _ver = __import__('sys').version_info
            is_py3 = (_ver[0] == 3)
            if is_py3:location = location.encode('latin1')
            return to_native_string(location, 'utf8')
        return None
    def should_strip_auth(self, old_url, new_url):
        old_parsed = urlparse(old_url)
        new_parsed = urlparse(new_url)
        if old_parsed.hostname != new_parsed.hostname:return True
        if (old_parsed.scheme == 'http' and old_parsed.port in (80, None) and new_parsed.scheme == 'https' and new_parsed.port in (443, None)):
            return False
        changed_port = old_parsed.port != new_parsed.port
        changed_scheme = old_parsed.scheme != new_parsed.scheme
        default_port = (DEFAULT_PORTS.get(old_parsed.scheme, None), None)
        if (not changed_scheme and old_parsed.port in default_port and new_parsed.port in default_port):
            return False
        return changed_port or changed_scheme
    def resolve_redirects(self, resp, req, stream=False, timeout=None,
                          verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs):
        hist = []
        url = self.get_redirect_target(resp)
        previous_fragment = urlparse(req.url).fragment
        while url:
            prepared_request = req.copy()
            hist.append(resp)
            resp.history = hist[1:]
            try:resp.content
            except (ChunkedEncodingError, ContentDecodingError, RuntimeError):resp.raw.read(decode_content=False)
            if len(resp.history) >= self.max_redirects:raise TooManyRedirects('Exceeded {} redirects.'.format(self.max_redirects), response=resp)
            resp.close()
            if url.startswith('//'):
                parsed_rurl = urlparse(resp.url)
                url = ':'.join([to_native_string(parsed_rurl.scheme), url])
            parsed = urlparse(url)
            if parsed.fragment == '' and previous_fragment:parsed = parsed._replace(fragment=previous_fragment)
            elif parsed.fragment:previous_fragment = parsed.fragment
            url = parsed.geturl()
            if not parsed.netloc:url = urljoin(resp.url, requote_uri(url))
            else:url = requote_uri(url)
            prepared_request.url = to_native_string(url)
            self.rebuild_method(prepared_request, resp)
            if resp.status_code not in (codes.temporary_redirect, codes.permanent_redirect):
                purged_headers = ('Content-Length', 'Content-Type', 'Transfer-Encoding')
                for header in purged_headers:prepared_request.headers.pop(header, None)
                prepared_request.body = None
            headers = prepared_request.headers
            headers.pop('Cookie', None)
            extract_cookies_to_jar(prepared_request._cookies, req, resp.raw)
            merge_cookies(prepared_request._cookies, self.cookies)
            prepared_request.prepare_cookies(prepared_request._cookies)
            proxies = self.rebuild_proxies(prepared_request, proxies)
            self.rebuild_auth(prepared_request, resp)
            rewindable = (
                prepared_request._body_position is not None and
                ('Content-Length' in headers or 'Transfer-Encoding' in headers)
            )
            if rewindable:rewind_body(prepared_request)
            req = prepared_request
            if yield_requests:yield req
            else:
                resp = self.send(
                    req,
                    stream=stream,
                    timeout=timeout,
                    verify=verify,
                    cert=cert,
                    proxies=proxies,
                    allow_redirects=False,
                    **adapter_kwargs
                )
                extract_cookies_to_jar(self.cookies, prepared_request, resp.raw)
                url = self.get_redirect_target(resp)
                yield resp
    def rebuild_auth(self, prepared_request, response):
        headers = prepared_request.headers
        url = prepared_request.url
        if 'Authorization' in headers and self.should_strip_auth(response.request.url, url):del headers['Authorization']
        new_auth = get_netrc_auth(url) if self.trust_env else None
        if new_auth is not None:prepared_request.prepare_auth(new_auth)
    def rebuild_proxies(self, prepared_request, proxies):
        proxies = proxies if proxies is not None else {}
        headers = prepared_request.headers
        url = prepared_request.url
        scheme = urlparse(url).scheme
        new_proxies = proxies.copy()
        no_proxy = proxies.get('no_proxy')
        bypass_proxy = should_bypass_proxies(url, no_proxy=no_proxy)
        if self.trust_env and not bypass_proxy:
            environ_proxies = get_environ_proxies(url, no_proxy=no_proxy)
            proxy = environ_proxies.get(scheme, environ_proxies.get('all'))
            if proxy:new_proxies.setdefault(scheme, proxy)
        if 'Proxy-Authorization' in headers:del headers['Proxy-Authorization']
        try:username, password = get_auth_from_url(new_proxies[scheme])
        except KeyError:username, password = None, None
        if not scheme.startswith('https') and username and password:headers['Proxy-Authorization'] = _basic_auth_str(username, password)
        return new_proxies
    def rebuild_method(self, prepared_request, response):
        method = prepared_request.method
        if response.status_code == codes.see_other and method != 'HEAD':method = 'GET'
        if response.status_code == codes.found and method != 'HEAD':method = 'GET'
        if response.status_code == codes.moved and method == 'POST':method = 'GET'
        prepared_request.method = method
    def __enter__(self):return self
    def __exit__(self, *args):
        for v in self.adapters.values():v.close()
    def request(self, method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None):
        req = __import__('requests').models.Request(
            method=method.upper(),
            url=url,
            headers=headers,
            files=files,
            data=data or {},
            json=json,
            params=params or {},
            auth=auth,
            cookies=cookies,
            hooks=hooks,
        )
        cookies = req.cookies or {}
        if not isinstance(cookies, __import__('http').cookiejar.CookieJar):cookies = __import__('requests').cookies.cookiejar_from_dict(cookies)
        auth = req.auth
        if self.trust_env and not auth and not self.auth:auth = __import__('requests').utils.get_netrc_auth(req.url)
        prep = __import__('requests').models.PreparedRequest()
        prep.prepare(
            method=req.method.upper(),
            url=req.url,
            files=req.files,
            data=req.data,
            json=req.json,
            headers=self.merge_setting(req.headers, self.headers, dict_class=__import__('requests').structures.CaseInsensitiveDict),
            params=self.merge_setting(req.params, self.params),
            auth=self.merge_setting(auth, self.auth),
            cookies=__import__('requests').cookies.merge_cookies(__import__('requests').cookies.merge_cookies(__import__('requests').cookies.RequestsCookieJar(), self.cookies), cookies),
            hooks=self.merge_hooks(req.hooks, self.hooks),
        )
        send_kwargs = {'timeout': timeout,'allow_redirects': allow_redirects,}
        url = prep.url
        stream = stream
        verify = verify
        cert = cert
        proxies = proxies or {}
        if self.trust_env:
            no_proxy = proxies.get('no_proxy') if proxies is not None else None
            env_proxies = __import__('requests').utils.get_environ_proxies(url, no_proxy=no_proxy)
            for (k, v) in env_proxies.items():proxies.setdefault(k, v)
            if verify is True or verify is None:verify = (__import__('os').environ.get('REQUESTS_CA_BUNDLE') or __import__('os').environ.get('CURL_CA_BUNDLE'))
        send_kwargs.update({'verify': self.merge_setting(verify, self.verify), 'proxies': self.merge_setting(proxies, self.proxies), 'stream': self.merge_setting(stream, self.stream), 'cert': self.merge_setting(cert, self.cert)})
        return self.send(prep, **send_kwargs)
    def get(self, url, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return self.request('GET', url, **kwargs)
    def post(self, url, data=None, json=None, **kwargs):
        return self.request('POST', url, data=data, json=json, **kwargs)
    def merge_setting(self, request_setting, session_setting, dict_class=None):
        if session_setting is None:return request_setting
        if request_setting is None:return session_setting
        if isinstance(session_setting, dict) and isinstance(request_setting, dict):
            result = dict_class(session_setting) if dict_class is not None else session_setting.copy()
            result.update(request_setting)
            return result
        return request_setting
    def merge_hooks(self, request_hooks, session_hooks):
        merged = {}
        for key in set(session_hooks.keys()).union(request_hooks.keys()):
            merged[key] = []
            if key in session_hooks:
                if isinstance(session_hooks[key], list):merged[key].extend(session_hooks[key])
                else:merged[key].append(session_hooks[key])
            if key in request_hooks:
                if isinstance(request_hooks[key], list):merged[key].extend(request_hooks[key])
                else:merged[key].append(request_hooks[key])
        return merged
    def send(self, request, **kwargs):
        kwargs.setdefault('stream', self.stream)
        kwargs.setdefault('verify', self.verify)
        kwargs.setdefault('cert', self.cert)
        kwargs.setdefault('proxies', self.proxies)
        if isinstance(request, __import__('requests').models.Request):raise ValueError('You can only send PreparedRequests.')
        allow_redirects = kwargs.pop('allow_redirects', True)
        start = self.preferred_clock()
        urls = request.url
        try:
            for (prefix, adapter) in self.adapters.items():
                if urls.lower().startswith(prefix.lower()):r = adapter.send(request, **kwargs)
        except:raise __import__('requests').exceptions.InvalidSchema("No connection adapters were found for {!r}".format(urls))
        elapsed = self.preferred_clock() - start
        r.elapsed = __import__('datetime').timedelta(seconds=elapsed)
        hooks = request.hooks or {}
        hooks = hooks.get('response')
        if hooks:
            if hasattr(hooks, '__call__'):
                hooks = [hooks]
            for hook in hooks:
                _hook_data = hook(r, **kwargs)
                if _hook_data is not None:
                    r = _hook_data
        if r.history:
            for resp in r.history:__import__('requests').cookies.extract_cookies_to_jar(self.cookies, resp.request, resp.raw)
        __import__('requests').cookies.extract_cookies_to_jar(self.cookies, request, r.raw)
        if allow_redirects:history = [resp for resp in self.resolve_redirects(r, request, **kwargs)]
        else:history = []
        if history:
            history.insert(0, r)
            r = history.pop()
            r.history = history
        if not allow_redirects:
            try:r._next = next(self.resolve_redirects(r, request, yield_requests=True, **kwargs))
            except StopIteration:pass
        if not kwargs.get('stream'):r.content
        return r
    def mount(self, prefix, adapter):
        self.adapters[prefix] = adapter
        keys_to_move = [k for k in self.adapters if len(k) < len(prefix)]
        for key in keys_to_move:self.adapters[key] = self.adapters.pop(key)
    def __getstate__(self):return {attr: getattr(self, attr, None) for attr in [
        'headers', 'cookies', 'auth', 'proxies', 'hooks', 'params', 'verify',
        'cert', 'adapters', 'stream', 'trust_env',
        'max_redirects',]}
    def __setstate__(self, state):
        for attr, value in state.items():setattr(self, attr, value)
def request(method, url, **kwargs):
    with Session() as session:
        return session.request(method=method, url=url, **kwargs)
def get(url, params=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
import datetime
import encodings.idna
from io import UnsupportedOperation
from urllib3.exceptions import DecodeError, LocationParseError, ProtocolError, ReadTimeoutError, SSLError
from urllib3.fields import RequestField
from urllib3.filepost import encode_multipart_formdata
from urllib3.util import parse_url
from requests.auth import HTTPBasicAuth
from requests.compat import Callable, JSONDecodeError, Mapping, basestring, builtin_str, chardet, cookielib
from requests.compat import json as complexjson
from requests.compat import urlencode, urlsplit, urlunparse
from requests.cookies import _copy_cookie_jar, cookiejar_from_dict, get_cookie_header
from requests.exceptions import ChunkedEncodingError, ConnectionError, ContentDecodingError, HTTPError, InvalidJSONError, InvalidURL
from requests.exceptions import JSONDecodeError as RequestsJSONDecodeError
from requests.exceptions import MissingSchema
from requests.exceptions import SSLError as RequestsSSLError
from requests.exceptions import StreamConsumedError
from requests.hooks import default_hooks
from requests.structures import CaseInsensitiveDict
from requests._internal_utils import to_native_string, unicode_is_ascii
from requests.utils import check_header_validity, get_auth_from_url, guess_filename, guess_json_utf, iter_slices, parse_header_links, requote_uri, stream_decode_response_unicode, super_len, to_key_val_list
REDIRECT_STATI = (codes.moved, codes.found, codes.other, codes.temporary_redirect, codes.permanent_redirect)
DEFAULT_REDIRECT_LIMIT = 30
CONTENT_CHUNK_SIZE = 10 * 1024
ITER_CHUNK_SIZE = 512

class RequestEncodingMixin:

    @property
    def path_url(self):
        url = []
        p = urlsplit(self.url)
        path = p.path
        if not path:
            path = '/'
        url.append(path)
        query = p.query
        if query:
            url.append('?')
            url.append(query)
        return ''.join(url)

    @staticmethod
    def _encode_params(data):
        if isinstance(data, (str, bytes)):
            return data
        elif hasattr(data, 'read'):
            return data
        elif hasattr(data, '__iter__'):
            result = []
            for k, vs in to_key_val_list(data):
                if isinstance(vs, basestring) or not hasattr(vs, '__iter__'):
                    vs = [vs]
                for v in vs:
                    if v is not None:
                        result.append((k.encode('utf-8') if isinstance(k, str) else k, v.encode('utf-8') if isinstance(v, str) else v))
            return urlencode(result, doseq=True)
        else:
            return data

    @staticmethod
    def _encode_files(files, data):
        if not files:
            raise ValueError('Files must be provided.')
        elif isinstance(data, basestring):
            raise ValueError('Data must not be a string.')
        new_fields = []
        fields = to_key_val_list(data or {})
        files = to_key_val_list(files or {})
        for field, val in fields:
            if isinstance(val, basestring) or not hasattr(val, '__iter__'):
                val = [val]
            for v in val:
                if v is not None:
                    if not isinstance(v, bytes):
                        v = str(v)
                    new_fields.append((field.decode('utf-8') if isinstance(field, bytes) else field, v.encode('utf-8') if isinstance(v, str) else v))
        for k, v in files:
            ft = None
            fh = None
            if isinstance(v, (tuple, list)):
                if len(v) == 2:
                    fn, fp = v
                elif len(v) == 3:
                    fn, fp, ft = v
                else:
                    fn, fp, ft, fh = v
            else:
                fn = guess_filename(v) or k
                fp = v
            if isinstance(fp, (str, bytes, bytearray)):
                fdata = fp
            elif hasattr(fp, 'read'):
                fdata = fp.read()
            elif fp is None:
                continue
            else:
                fdata = fp
            rf = RequestField(name=k, data=fdata, filename=fn, headers=fh)
            rf.make_multipart(content_type=ft)
            new_fields.append(rf)
        body, content_type = encode_multipart_formdata(new_fields)
        return (body, content_type)

class RequestHooksMixin:

    def register_hook(self, event, hook):
        if event not in self.hooks:
            raise ValueError(f'Unsupported event specified, with event name "{event}"')
        if isinstance(hook, Callable):
            self.hooks[event].append(hook)
        elif hasattr(hook, '__iter__'):
            self.hooks[event].extend((h for h in hook if isinstance(h, Callable)))

    def deregister_hook(self, event, hook):
        try:
            self.hooks[event].remove(hook)
            return True
        except ValueError:
            return False

class Request(RequestHooksMixin):

    def __init__(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None):
        data = [] if data is None else data
        files = [] if files is None else files
        headers = {} if headers is None else headers
        params = {} if params is None else params
        hooks = {} if hooks is None else hooks
        self.hooks = default_hooks()
        for k, v in list(hooks.items()):
            self.register_hook(event=k, hook=v)
        self.method = method
        self.url = url
        self.headers = headers
        self.files = files
        self.data = data
        self.json = json
        self.params = params
        self.auth = auth
        self.cookies = cookies

    def __repr__(self):
        return f'<Request [{self.method}]>'

    def prepare(self):
        p = PreparedRequest()
        p.prepare(method=self.method, url=self.url, headers=self.headers, files=self.files, data=self.data, json=self.json, params=self.params, auth=self.auth, cookies=self.cookies, hooks=self.hooks)
        return p

class PreparedRequest(RequestEncodingMixin, RequestHooksMixin):

    def __init__(self):
        self.method = None
        self.url = None
        self.headers = None
        self._cookies = None
        self.body = None
        self.hooks = default_hooks()
        self._body_position = None

    def prepare(self, method=None, url=None, headers=None, files=None, data=None, params=None, auth=None, cookies=None, hooks=None, json=None):
        self.prepare_method(method)
        self.prepare_url(url, params)
        self.prepare_headers(headers)
        self.prepare_cookies(cookies)
        self.prepare_body(data, files, json)
        self.prepare_auth(auth, url)
        self.prepare_hooks(hooks)

    def __repr__(self):
        return f'<PreparedRequest [{self.method}]>'

    def copy(self):
        p = PreparedRequest()
        p.method = self.method
        p.url = self.url
        p.headers = self.headers.copy() if self.headers is not None else None
        p._cookies = _copy_cookie_jar(self._cookies)
        p.body = self.body
        p.hooks = self.hooks
        p._body_position = self._body_position
        return p

    def prepare_method(self, method):
        self.method = method
        if self.method is not None:
            self.method = to_native_string(self.method.upper())

    @staticmethod
    def _get_idna_encoded_host(host):
        import idna
        try:
            host = idna.encode(host, uts46=True).decode('utf-8')
        except idna.IDNAError:
            raise UnicodeError
        return host

    def prepare_url(self, url, params):
        if isinstance(url, bytes):
            url = url.decode('utf8')
        else:
            url = str(url)
        url = url.lstrip()
        if ':' in url and (not url.lower().startswith('http')):
            self.url = url
            return
        try:
            scheme, auth, host, port, path, query, fragment = parse_url(url)
        except LocationParseError as e:
            raise InvalidURL(*e.args)
        if not scheme:
            raise MissingSchema(f'Invalid URL {url!r}: No scheme supplied. Perhaps you meant https://{url}?')
        if not host:
            raise InvalidURL(f'Invalid URL {url!r}: No host supplied')
        if not unicode_is_ascii(host):
            try:
                host = self._get_idna_encoded_host(host)
            except UnicodeError:
                raise InvalidURL('URL has an invalid label.')
        elif host.startswith(('*', '.')):
            raise InvalidURL('URL has an invalid label.')
        netloc = auth or ''
        if netloc:
            netloc += '@'
        netloc += host
        if port:
            netloc += f':{port}'
        if not path:
            path = '/'
        if isinstance(params, (str, bytes)):
            params = to_native_string(params)
        enc_params = self._encode_params(params)
        if enc_params:
            if query:
                query = f'{query}&{enc_params}'
            else:
                query = enc_params
        url = requote_uri(urlunparse([scheme, netloc, path, None, query, fragment]))
        self.url = url

    def prepare_headers(self, headers):
        self.headers = CaseInsensitiveDict()
        if headers:
            for header in headers.items():
                check_header_validity(header)
                name, value = header
                self.headers[to_native_string(name)] = value

    def prepare_body(self, data, files, json=None):
        body = None
        content_type = None
        if not data and json is not None:
            content_type = 'application/json'
            try:
                body = complexjson.dumps(json, allow_nan=False)
            except ValueError as ve:
                raise InvalidJSONError(ve, request=self)
            if not isinstance(body, bytes):
                body = body.encode('utf-8')
        is_stream = all([hasattr(data, '__iter__'), not isinstance(data, (basestring, list, tuple, Mapping))])
        if is_stream:
            try:
                length = super_len(data)
            except (TypeError, AttributeError, UnsupportedOperation):
                length = None
            body = data
            if getattr(body, 'tell', None) is not None:
                try:
                    self._body_position = body.tell()
                except OSError:
                    self._body_position = object()
            if files:
                raise NotImplementedError('Streamed bodies and files are mutually exclusive.')
            if length:
                self.headers['Content-Length'] = builtin_str(length)
            else:
                self.headers['Transfer-Encoding'] = 'chunked'
        else:
            if files:
                body, content_type = self._encode_files(files, data)
            elif data:
                body = self._encode_params(data)
                if isinstance(data, basestring) or hasattr(data, 'read'):
                    content_type = None
                else:
                    content_type = 'application/x-www-form-urlencoded'
            self.prepare_content_length(body)
            if content_type and 'content-type' not in self.headers:
                self.headers['Content-Type'] = content_type
        self.body = body

    def prepare_content_length(self, body):
        if body is not None:
            length = super_len(body)
            if length:
                self.headers['Content-Length'] = builtin_str(length)
        elif self.method not in ('GET', 'HEAD') and self.headers.get('Content-Length') is None:
            self.headers['Content-Length'] = '0'

    def prepare_auth(self, auth, url=''):
        if auth is None:
            url_auth = get_auth_from_url(self.url)
            auth = url_auth if any(url_auth) else None
        if auth:
            if isinstance(auth, tuple) and len(auth) == 2:
                auth = HTTPBasicAuth(*auth)
            r = auth(self)
            self.__dict__.update(r.__dict__)
            self.prepare_content_length(self.body)

    def prepare_cookies(self, cookies):
        if isinstance(cookies, cookielib.CookieJar):
            self._cookies = cookies
        else:
            self._cookies = cookiejar_from_dict(cookies)
        cookie_header = get_cookie_header(self._cookies, self)
        if cookie_header is not None:
            self.headers['Cookie'] = cookie_header

    def prepare_hooks(self, hooks):
        hooks = hooks or []
        for event in hooks:
            self.register_hook(event, hooks[event])

class Response:
    __attrs__ = ['_content', 'status_code', 'headers', 'url', 'history', 'encoding', 'reason', 'cookies', 'elapsed', 'request']

    def __init__(self):
        self._content = False
        self._content_consumed = False
        self._next = None
        self.status_code = None
        self.headers = CaseInsensitiveDict()
        self.raw = None
        self.url = None
        self.encoding = None
        self.history = []
        self.reason = None
        self.cookies = cookiejar_from_dict({})
        self.elapsed = datetime.timedelta(0)
        self.request = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __getstate__(self):
        if not self._content_consumed:
            self.content
        return {attr: getattr(self, attr, None) for attr in self.__attrs__}

    def __setstate__(self, state):
        for name, value in state.items():
            setattr(self, name, value)
        setattr(self, '_content_consumed', True)
        setattr(self, 'raw', None)

    def __repr__(self):
        return f'<Response [{self.status_code}]>'

    def __bool__(self):
        return self.ok

    def __nonzero__(self):
        return self.ok

    def __iter__(self):
        return self.iter_content(128)

    @property
    def ok(self):
        try:
            self.raise_for_status()
        except HTTPError:
            return False
        return True

    @property
    def is_redirect(self):
        return 'location' in self.headers and self.status_code in REDIRECT_STATI

    @property
    def is_permanent_redirect(self):
        return 'location' in self.headers and self.status_code in (codes.moved_permanently, codes.permanent_redirect)

    @property
    def next(self):
        return self._next

    @property
    def apparent_encoding(self):
        if chardet is not None:
            return chardet.detect(self.content)['encoding']
        else:
            return 'utf-8'

    def iter_content(self, chunk_size=1, decode_unicode=False):

        def generate():
            if hasattr(self.raw, 'stream'):
                try:
                    yield from self.raw.stream(chunk_size, decode_content=True)
                except ProtocolError as e:
                    raise ChunkedEncodingError(e)
                except DecodeError as e:
                    raise ContentDecodingError(e)
                except ReadTimeoutError as e:
                    raise ConnectionError(e)
                except SSLError as e:
                    raise RequestsSSLError(e)
            else:
                while True:
                    chunk = self.raw.read(chunk_size)
                    if not chunk:
                        break
                    yield chunk
            self._content_consumed = True
        if self._content_consumed and isinstance(self._content, bool):
            raise StreamConsumedError()
        elif chunk_size is not None and (not isinstance(chunk_size, int)):
            raise TypeError(f'chunk_size must be an int, it is instead a {type(chunk_size)}.')
        reused_chunks = iter_slices(self._content, chunk_size)
        stream_chunks = generate()
        chunks = reused_chunks if self._content_consumed else stream_chunks
        if decode_unicode:
            chunks = stream_decode_response_unicode(chunks, self)
        return chunks

    def iter_lines(self, chunk_size=ITER_CHUNK_SIZE, decode_unicode=False, delimiter=None):
        pending = None
        for chunk in self.iter_content(chunk_size=chunk_size, decode_unicode=decode_unicode):
            if pending is not None:
                chunk = pending + chunk
            if delimiter:
                lines = chunk.split(delimiter)
            else:
                lines = chunk.splitlines()
            if lines and lines[-1] and chunk and (lines[-1][-1] == chunk[-1]):
                pending = lines.pop()
            else:
                pending = None
            yield from lines
        if pending is not None:
            yield pending

    @property
    def content(self):
        if self._content is False:
            if self._content_consumed:
                raise RuntimeError('The content for this response was already consumed')
            if self.status_code == 0 or self.raw is None:
                self._content = None
            else:
                self._content = b''.join(self.iter_content(CONTENT_CHUNK_SIZE)) or b''
        self._content_consumed = True
        return self._content

    @property
    def text(self):
        content = None
        encoding = self.encoding
        if not self.content:
            return ''
        if self.encoding is None:
            encoding = self.apparent_encoding
        try:
            content = str(self.content, encoding, errors='replace')
        except (LookupError, TypeError):
            content = str(self.content, errors='replace')
        return content

    def json(self, **kwargs):
        if not self.encoding and self.content and (len(self.content) > 3):
            encoding = guess_json_utf(self.content)
            if encoding is not None:
                try:
                    return complexjson.loads(self.content.decode(encoding), **kwargs)
                except UnicodeDecodeError:
                    pass
                except JSONDecodeError as e:
                    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
        try:
            return complexjson.loads(self.text, **kwargs)
        except JSONDecodeError as e:
            raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)

    @property
    def links(self):
        header = self.headers.get('link')
        resolved_links = {}
        if header:
            links = parse_header_links(header)
            for link in links:
                key = link.get('rel') or link.get('url')
                resolved_links[key] = link
        return resolved_links

    def raise_for_status(self):
        http_error_msg = ''
        if isinstance(self.reason, bytes):
            try:
                reason = self.reason.decode('utf-8')
            except UnicodeDecodeError:
                reason = self.reason.decode('iso-8859-1')
        else:
            reason = self.reason
        if 400 <= self.status_code < 500:
            http_error_msg = f'{self.status_code} Client Error: {reason} for url: {self.url}'
        elif 500 <= self.status_code < 600:
            http_error_msg = f'{self.status_code} Server Error: {reason} for url: {self.url}'
        if http_error_msg:
            raise HTTPError(http_error_msg, response=self)

    def close(self):
        if not self._content_consumed:
            self.raw.close()
        release_conn = getattr(self.raw, 'release_conn', None)
        if release_conn is not None:
            release_conn()
def put(url, data=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('put', url, data=data, **kwargs)

def patch(url, data=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('patch', url, data=data, **kwargs)

def delete(url, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('delete', url, **kwargs)

def head(url, **kwargs):
    kwargs.setdefault('allow_redirects', False)
    return request('head', url, **kwargs)

def options(url, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('options', url, **kwargs)

def session():
    return Session()
import codecs
import contextlib
import io
import os
import re
import socket
import struct
import sys
import tempfile
import warnings
import zipfile
from collections import OrderedDict
from urllib3.util import make_headers, parse_url
from requests import certs
from requests.__version__ import __version__
from requests._internal_utils import _HEADER_VALIDATORS_BYTE, _HEADER_VALIDATORS_STR, HEADER_VALIDATORS, to_native_string
from requests.compat import Mapping, basestring, bytes, getproxies, getproxies_environment, integer_types, is_urllib3_1
from requests.compat import parse_http_list as _parse_list_header
from requests.compat import proxy_bypass, proxy_bypass_environment, quote, str, unquote, urlparse, urlunparse
from requests.cookies import cookiejar_from_dict
from requests.exceptions import FileModeWarning, InvalidHeader, InvalidURL, UnrewindableBodyError
from requests.structures import CaseInsensitiveDict
NETRC_FILES = ('.netrc', '_netrc')
DEFAULT_CA_BUNDLE_PATH = certs.where()
DEFAULT_PORTS = {'http': 80, 'https': 443}
DEFAULT_ACCEPT_ENCODING = ', '.join(re.split(',\\s*', make_headers(accept_encoding=True)['accept-encoding']))
if sys.platform == 'win32':

    def proxy_bypass_registry(host):
        try:
            import winreg
        except ImportError:
            return False
        try:
            internetSettings = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings')
            proxyEnable = int(winreg.QueryValueEx(internetSettings, 'ProxyEnable')[0])
            proxyOverride = winreg.QueryValueEx(internetSettings, 'ProxyOverride')[0]
        except (OSError, ValueError):
            return False
        if not proxyEnable or not proxyOverride:
            return False
        proxyOverride = proxyOverride.split(';')
        proxyOverride = filter(None, proxyOverride)
        for test in proxyOverride:
            if test == '<local>':
                if '.' not in host:
                    return True
            test = test.replace('.', '\\.')
            test = test.replace('*', '.*')
            test = test.replace('?', '.')
            if re.match(test, host, re.I):
                return True
        return False

    def proxy_bypass(host):
        if getproxies_environment():
            return proxy_bypass_environment(host)
        else:
            return proxy_bypass_registry(host)

def dict_to_sequence(d):
    if hasattr(d, 'items'):
        d = d.items()
    return d

def super_len(o):
    total_length = None
    current_position = 0
    if not is_urllib3_1 and isinstance(o, str):
        o = o.encode('utf-8')
    if hasattr(o, '__len__'):
        total_length = len(o)
    elif hasattr(o, 'len'):
        total_length = o.len
    elif hasattr(o, 'fileno'):
        try:
            fileno = o.fileno()
        except (io.UnsupportedOperation, AttributeError):
            pass
        else:
            total_length = os.fstat(fileno).st_size
            if 'b' not in o.mode:
                warnings.warn("Requests has determined the content-length for this request using the binary size of the file: however, the file has been opened in text mode (i.e. without the 'b' flag in the mode). This may lead to an incorrect content-length. In Requests 3.0, support will be removed for files in text mode.", FileModeWarning)
    if hasattr(o, 'tell'):
        try:
            current_position = o.tell()
        except OSError:
            if total_length is not None:
                current_position = total_length
        else:
            if hasattr(o, 'seek') and total_length is None:
                try:
                    o.seek(0, 2)
                    total_length = o.tell()
                    o.seek(current_position or 0)
                except OSError:
                    total_length = 0
    if total_length is None:
        total_length = 0
    return max(0, total_length - current_position)

def get_netrc_auth(url, raise_errors=False):
    netrc_file = os.environ.get('NETRC')
    if netrc_file is not None:
        netrc_locations = (netrc_file,)
    else:
        netrc_locations = (f'~/{f}' for f in NETRC_FILES)
    try:
        from netrc import NetrcParseError, netrc
        netrc_path = None
        for f in netrc_locations:
            loc = os.path.expanduser(f)
            if os.path.exists(loc):
                netrc_path = loc
                break
        if netrc_path is None:
            return
        ri = urlparse(url)
        host = ri.hostname
        try:
            _netrc = netrc(netrc_path).authenticators(host)
            if _netrc:
                login_i = 0 if _netrc[0] else 1
                return (_netrc[login_i], _netrc[2])
        except (NetrcParseError, OSError):
            if raise_errors:
                raise
    except (ImportError, AttributeError):
        pass

def guess_filename(obj):
    name = getattr(obj, 'name', None)
    if name and isinstance(name, basestring) and (name[0] != '<') and (name[-1] != '>'):
        return os.path.basename(name)

def extract_zipped_paths(path):
    if os.path.exists(path):
        return path
    archive, member = os.path.split(path)
    while archive and (not os.path.exists(archive)):
        archive, prefix = os.path.split(archive)
        if not prefix:
            break
        member = '/'.join([prefix, member])
    if not zipfile.is_zipfile(archive):
        return path
    zip_file = zipfile.ZipFile(archive)
    if member not in zip_file.namelist():
        return path
    tmp = tempfile.gettempdir()
    extracted_path = os.path.join(tmp, member.split('/')[-1])
    if not os.path.exists(extracted_path):
        with atomic_open(extracted_path) as file_handler:
            file_handler.write(zip_file.read(member))
    return extracted_path

@contextlib.contextmanager
def atomic_open(filename):
    tmp_descriptor, tmp_name = tempfile.mkstemp(dir=os.path.dirname(filename))
    try:
        with os.fdopen(tmp_descriptor, 'wb') as tmp_handler:
            yield tmp_handler
        os.replace(tmp_name, filename)
    except BaseException:
        os.remove(tmp_name)
        raise

def from_key_val_list(value):
    if value is None:
        return None
    if isinstance(value, (str, bytes, bool, int)):
        raise ValueError('cannot encode objects that are not 2-tuples')
    return OrderedDict(value)

def to_key_val_list(value):
    if value is None:
        return None
    if isinstance(value, (str, bytes, bool, int)):
        raise ValueError('cannot encode objects that are not 2-tuples')
    if isinstance(value, Mapping):
        value = value.items()
    return list(value)

def parse_list_header(value):
    result = []
    for item in _parse_list_header(value):
        if item[:1] == item[-1:] == '"':
            item = unquote_header_value(item[1:-1])
        result.append(item)
    return result

def parse_dict_header(value):
    result = {}
    for item in _parse_list_header(value):
        if '=' not in item:
            result[item] = None
            continue
        name, value = item.split('=', 1)
        if value[:1] == value[-1:] == '"':
            value = unquote_header_value(value[1:-1])
        result[name] = value
    return result

def unquote_header_value(value, is_filename=False):
    if value and value[0] == value[-1] == '"':
        value = value[1:-1]
        if not is_filename or value[:2] != '\\\\':
            return value.replace('\\\\', '\\').replace('\\"', '"')
    return value

def dict_from_cookiejar(cj):
    cookie_dict = {cookie.name: cookie.value for cookie in cj}
    return cookie_dict

def add_dict_to_cookiejar(cj, cookie_dict):
    return cookiejar_from_dict(cookie_dict, cj)

def get_encodings_from_content(content):
    warnings.warn('In requests 3.0, get_encodings_from_content will be removed. For more information, please see the discussion on issue #2266. (This warning should only appear once.)', DeprecationWarning)
    charset_re = re.compile('<meta.*?charset=["\\\']*(.+?)["\\\'>]', flags=re.I)
    pragma_re = re.compile('<meta.*?content=["\\\']*;?charset=(.+?)["\\\'>]', flags=re.I)
    xml_re = re.compile('^<\\?xml.*?encoding=["\\\']*(.+?)["\\\'>]')
    return charset_re.findall(content) + pragma_re.findall(content) + xml_re.findall(content)

def _parse_content_type_header(header):
    tokens = header.split(';')
    content_type, params = (tokens[0].strip(), tokens[1:])
    params_dict = {}
    items_to_strip = '"\' '
    for param in params:
        param = param.strip()
        if param:
            key, value = (param, True)
            index_of_equals = param.find('=')
            if index_of_equals != -1:
                key = param[:index_of_equals].strip(items_to_strip)
                value = param[index_of_equals + 1:].strip(items_to_strip)
            params_dict[key.lower()] = value
    return (content_type, params_dict)

def get_encoding_from_headers(headers):
    content_type = headers.get('content-type')
    if not content_type:
        return None
    content_type, params = _parse_content_type_header(content_type)
    if 'charset' in params:
        return params['charset'].strip('\'"')
    if 'text' in content_type:
        return 'ISO-8859-1'
    if 'application/json' in content_type:
        return 'utf-8'

def stream_decode_response_unicode(iterator, r):
    if r.encoding is None:
        yield from iterator
        return
    decoder = codecs.getincrementaldecoder(r.encoding)(errors='replace')
    for chunk in iterator:
        rv = decoder.decode(chunk)
        if rv:
            yield rv
    rv = decoder.decode(b'', final=True)
    if rv:
        yield rv

def iter_slices(string, slice_length):
    pos = 0
    if slice_length is None or slice_length <= 0:
        slice_length = len(string)
    while pos < len(string):
        yield string[pos:pos + slice_length]
        pos += slice_length

def get_unicode_from_response(r):
    warnings.warn('In requests 3.0, get_unicode_from_response will be removed. For more information, please see the discussion on issue #2266. (This warning should only appear once.)', DeprecationWarning)
    tried_encodings = []
    encoding = get_encoding_from_headers(r.headers)
    if encoding:
        try:
            return str(r.content, encoding)
        except UnicodeError:
            tried_encodings.append(encoding)
    try:
        return str(r.content, encoding, errors='replace')
    except TypeError:
        return r.content
UNRESERVED_SET = frozenset('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + '0123456789-._~')

def unquote_unreserved(uri):
    parts = uri.split('%')
    for i in range(1, len(parts)):
        h = parts[i][0:2]
        if len(h) == 2 and h.isalnum():
            try:
                c = chr(int(h, 16))
            except ValueError:
                raise InvalidURL(f"Invalid percent-escape sequence: '{h}'")
            if c in UNRESERVED_SET:
                parts[i] = c + parts[i][2:]
            else:
                parts[i] = f'%{parts[i]}'
        else:
            parts[i] = f'%{parts[i]}'
    return ''.join(parts)

def requote_uri(uri):
    safe_with_percent = "!#$%&'()*+,/:;=?@[]~"
    safe_without_percent = "!#$&'()*+,/:;=?@[]~"
    try:
        return quote(unquote_unreserved(uri), safe=safe_with_percent)
    except InvalidURL:
        return quote(uri, safe=safe_without_percent)

def address_in_network(ip, net):
    ipaddr = struct.unpack('=L', socket.inet_aton(ip))[0]
    netaddr, bits = net.split('/')
    netmask = struct.unpack('=L', socket.inet_aton(dotted_netmask(int(bits))))[0]
    network = struct.unpack('=L', socket.inet_aton(netaddr))[0] & netmask
    return ipaddr & netmask == network & netmask

def dotted_netmask(mask):
    bits = 4294967295 ^ (1 << 32 - mask) - 1
    return socket.inet_ntoa(struct.pack('>I', bits))

def is_ipv4_address(string_ip):
    try:
        socket.inet_aton(string_ip)
    except OSError:
        return False
    return True

def is_valid_cidr(string_network):
    if string_network.count('/') == 1:
        try:
            mask = int(string_network.split('/')[1])
        except ValueError:
            return False
        if mask < 1 or mask > 32:
            return False
        try:
            socket.inet_aton(string_network.split('/')[0])
        except OSError:
            return False
    else:
        return False
    return True

@contextlib.contextmanager
def set_environ(env_name, value):
    value_changed = value is not None
    if value_changed:
        old_value = os.environ.get(env_name)
        os.environ[env_name] = value
    try:
        yield
    finally:
        if value_changed:
            if old_value is None:
                del os.environ[env_name]
            else:
                os.environ[env_name] = old_value

def should_bypass_proxies(url, no_proxy):

    def get_proxy(key):
        return os.environ.get(key) or os.environ.get(key.upper())
    no_proxy_arg = no_proxy
    if no_proxy is None:
        no_proxy = get_proxy('no_proxy')
    parsed = urlparse(url)
    if parsed.hostname is None:
        return True
    if no_proxy:
        no_proxy = (host for host in no_proxy.replace(' ', '').split(',') if host)
        if is_ipv4_address(parsed.hostname):
            for proxy_ip in no_proxy:
                if is_valid_cidr(proxy_ip):
                    if address_in_network(parsed.hostname, proxy_ip):
                        return True
                elif parsed.hostname == proxy_ip:
                    return True
        else:
            host_with_port = parsed.hostname
            if parsed.port:
                host_with_port += f':{parsed.port}'
            for host in no_proxy:
                if parsed.hostname.endswith(host) or host_with_port.endswith(host):
                    return True
    with set_environ('no_proxy', no_proxy_arg):
        try:
            bypass = proxy_bypass(parsed.hostname)
        except (TypeError, socket.gaierror):
            bypass = False
    if bypass:
        return True
    return False

def get_environ_proxies(url, no_proxy=None):
    if should_bypass_proxies(url, no_proxy=no_proxy):
        return {}
    else:
        return getproxies()

def select_proxy(url, proxies):
    proxies = proxies or {}
    urlparts = urlparse(url)
    if urlparts.hostname is None:
        return proxies.get(urlparts.scheme, proxies.get('all'))
    proxy_keys = [urlparts.scheme + '://' + urlparts.hostname, urlparts.scheme, 'all://' + urlparts.hostname, 'all']
    proxy = None
    for proxy_key in proxy_keys:
        if proxy_key in proxies:
            proxy = proxies[proxy_key]
            break
    return proxy

def resolve_proxies(request, proxies, trust_env=True):
    proxies = proxies if proxies is not None else {}
    url = request.url
    scheme = urlparse(url).scheme
    no_proxy = proxies.get('no_proxy')
    new_proxies = proxies.copy()
    if trust_env and (not should_bypass_proxies(url, no_proxy=no_proxy)):
        environ_proxies = get_environ_proxies(url, no_proxy=no_proxy)
        proxy = environ_proxies.get(scheme, environ_proxies.get('all'))
        if proxy:
            new_proxies.setdefault(scheme, proxy)
    return new_proxies

def default_user_agent(name='python-requests'):
    return f'{name}/{__version__}'

def default_headers():
    return CaseInsensitiveDict({'User-Agent': default_user_agent(), 'Accept-Encoding': DEFAULT_ACCEPT_ENCODING, 'Accept': '*/*', 'Connection': 'keep-alive'})

def parse_header_links(value):
    links = []
    replace_chars = ' \'"'
    value = value.strip(replace_chars)
    if not value:
        return links
    for val in re.split(', *<', value):
        try:
            url, params = val.split(';', 1)
        except ValueError:
            url, params = (val, '')
        link = {'url': url.strip('<> \'"')}
        for param in params.split(';'):
            try:
                key, value = param.split('=')
            except ValueError:
                break
            link[key.strip(replace_chars)] = value.strip(replace_chars)
        links.append(link)
    return links
_null = '\x00'.encode('ascii')
_null2 = _null * 2
_null3 = _null * 3

def guess_json_utf(data):
    sample = data[:4]
    if sample in (codecs.BOM_UTF32_LE, codecs.BOM_UTF32_BE):
        return 'utf-32'
    if sample[:3] == codecs.BOM_UTF8:
        return 'utf-8-sig'
    if sample[:2] in (codecs.BOM_UTF16_LE, codecs.BOM_UTF16_BE):
        return 'utf-16'
    nullcount = sample.count(_null)
    if nullcount == 0:
        return 'utf-8'
    if nullcount == 2:
        if sample[::2] == _null2:
            return 'utf-16-be'
        if sample[1::2] == _null2:
            return 'utf-16-le'
    if nullcount == 3:
        if sample[:3] == _null3:
            return 'utf-32-be'
        if sample[1:] == _null3:
            return 'utf-32-le'
    return None

def prepend_scheme_if_needed(url, new_scheme):
    parsed = parse_url(url)
    scheme, auth, host, port, path, query, fragment = parsed
    netloc = parsed.netloc
    if not netloc:
        netloc, path = (path, netloc)
    if auth:
        netloc = '@'.join([auth, netloc])
    if scheme is None:
        scheme = new_scheme
    if path is None:
        path = ''
    return urlunparse((scheme, netloc, path, '', query, fragment))

def get_auth_from_url(url):
    parsed = urlparse(url)
    try:
        auth = (unquote(parsed.username), unquote(parsed.password))
    except (AttributeError, TypeError):
        auth = ('', '')
    return auth

def check_header_validity(header):
    name, value = header
    _validate_header_part(header, name, 0)
    _validate_header_part(header, value, 1)

def _validate_header_part(header, header_part, header_validator_index):
    if isinstance(header_part, str):
        validator = _HEADER_VALIDATORS_STR[header_validator_index]
    elif isinstance(header_part, bytes):
        validator = _HEADER_VALIDATORS_BYTE[header_validator_index]
    else:
        raise InvalidHeader(f'Header part ({header_part!r}) from {header} must be of type str or bytes, not {type(header_part)}')
    if not validator.match(header_part):
        header_kind = 'name' if header_validator_index == 0 else 'value'
        raise InvalidHeader(f'Invalid leading whitespace, reserved character(s), or return character(s) in header {header_kind}: {header_part!r}')

def urldefragauth(url):
    scheme, netloc, path, params, query, fragment = urlparse(url)
    if not netloc:
        netloc, path = (path, netloc)
    netloc = netloc.rsplit('@', 1)[-1]
    return urlunparse((scheme, netloc, path, params, query, ''))

def rewind_body(prepared_request):
    body_seek = getattr(prepared_request.body, 'seek', None)
    if body_seek is not None and isinstance(prepared_request._body_position, integer_types):
        try:
            body_seek(prepared_request._body_position)
        except OSError:
            raise UnrewindableBodyError('An error occurred when rewinding request body for redirect.')
    else:
        raise UnrewindableBodyError('Unable to rewind request body for redirect.')
import hashlib
import os
import re
import threading
import time
import warnings
from base64 import b64encode
from requests._internal_utils import to_native_string
from requests.compat import basestring, str, urlparse
from requests.cookies import extract_cookies_to_jar
from requests.utils import parse_dict_header
CONTENT_TYPE_FORM_URLENCODED = 'application/x-www-form-urlencoded'
CONTENT_TYPE_MULTI_PART = 'multipart/form-data'

def _basic_auth_str(username, password):
    if not isinstance(username, basestring):
        warnings.warn("Non-string usernames will no longer be supported in Requests 3.0.0. Please convert the object you've passed in ({!r}) to a string or bytes object in the near future to avoid problems.".format(username), category=DeprecationWarning)
        username = str(username)
    if not isinstance(password, basestring):
        warnings.warn("Non-string passwords will no longer be supported in Requests 3.0.0. Please convert the object you've passed in ({!r}) to a string or bytes object in the near future to avoid problems.".format(type(password)), category=DeprecationWarning)
        password = str(password)
    if isinstance(username, str):
        username = username.encode('latin1')
    if isinstance(password, str):
        password = password.encode('latin1')
    authstr = 'Basic ' + to_native_string(b64encode(b':'.join((username, password))).strip())
    return authstr

class AuthBase:

    def __call__(self, r):
        raise NotImplementedError('Auth hooks must be callable.')

class HTTPBasicAuth(AuthBase):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __eq__(self, other):
        return all([self.username == getattr(other, 'username', None), self.password == getattr(other, 'password', None)])

    def __ne__(self, other):
        return not self == other

    def __call__(self, r):
        r.headers['Authorization'] = _basic_auth_str(self.username, self.password)
        return r

class HTTPProxyAuth(HTTPBasicAuth):

    def __call__(self, r):
        r.headers['Proxy-Authorization'] = _basic_auth_str(self.username, self.password)
        return r

class HTTPDigestAuth(AuthBase):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self._thread_local = threading.local()

    def init_per_thread_state(self):
        if not hasattr(self._thread_local, 'init'):
            self._thread_local.init = True
            self._thread_local.last_nonce = ''
            self._thread_local.nonce_count = 0
            self._thread_local.chal = {}
            self._thread_local.pos = None
            self._thread_local.num_401_calls = None

    def build_digest_header(self, method, url):
        realm = self._thread_local.chal['realm']
        nonce = self._thread_local.chal['nonce']
        qop = self._thread_local.chal.get('qop')
        algorithm = self._thread_local.chal.get('algorithm')
        opaque = self._thread_local.chal.get('opaque')
        hash_utf8 = None
        if algorithm is None:
            _algorithm = 'MD5'
        else:
            _algorithm = algorithm.upper()
        if _algorithm == 'MD5' or _algorithm == 'MD5-SESS':

            def md5_utf8(x):
                if isinstance(x, str):
                    x = x.encode('utf-8')
                return hashlib.md5(x).hexdigest()
            hash_utf8 = md5_utf8
        elif _algorithm == 'SHA':

            def sha_utf8(x):
                if isinstance(x, str):
                    x = x.encode('utf-8')
                return hashlib.sha1(x).hexdigest()
            hash_utf8 = sha_utf8
        elif _algorithm == 'SHA-256':

            def sha256_utf8(x):
                if isinstance(x, str):
                    x = x.encode('utf-8')
                return hashlib.sha256(x).hexdigest()
            hash_utf8 = sha256_utf8
        elif _algorithm == 'SHA-512':

            def sha512_utf8(x):
                if isinstance(x, str):
                    x = x.encode('utf-8')
                return hashlib.sha512(x).hexdigest()
            hash_utf8 = sha512_utf8
        KD = lambda s, d: hash_utf8(f'{s}:{d}')
        if hash_utf8 is None:
            return None
        entdig = None
        p_parsed = urlparse(url)
        path = p_parsed.path or '/'
        if p_parsed.query:
            path += f'?{p_parsed.query}'
        A1 = f'{self.username}:{realm}:{self.password}'
        A2 = f'{method}:{path}'
        HA1 = hash_utf8(A1)
        HA2 = hash_utf8(A2)
        if nonce == self._thread_local.last_nonce:
            self._thread_local.nonce_count += 1
        else:
            self._thread_local.nonce_count = 1
        ncvalue = f'{self._thread_local.nonce_count:08x}'
        s = str(self._thread_local.nonce_count).encode('utf-8')
        s += nonce.encode('utf-8')
        s += time.ctime().encode('utf-8')
        s += os.urandom(8)
        cnonce = hashlib.sha1(s).hexdigest()[:16]
        if _algorithm == 'MD5-SESS':
            HA1 = hash_utf8(f'{HA1}:{nonce}:{cnonce}')
        if not qop:
            respdig = KD(HA1, f'{nonce}:{HA2}')
        elif qop == 'auth' or 'auth' in qop.split(','):
            noncebit = f'{nonce}:{ncvalue}:{cnonce}:auth:{HA2}'
            respdig = KD(HA1, noncebit)
        else:
            return None
        self._thread_local.last_nonce = nonce
        base = f'username="{self.username}", realm="{realm}", nonce="{nonce}", uri="{path}", response="{respdig}"'
        if opaque:
            base += f', opaque="{opaque}"'
        if algorithm:
            base += f', algorithm="{algorithm}"'
        if entdig:
            base += f', digest="{entdig}"'
        if qop:
            base += f', qop="auth", nc={ncvalue}, cnonce="{cnonce}"'
        return f'Digest {base}'

    def handle_redirect(self, r, **kwargs):
        if r.is_redirect:
            self._thread_local.num_401_calls = 1

    def handle_401(self, r, **kwargs):
        if not 400 <= r.status_code < 500:
            self._thread_local.num_401_calls = 1
            return r
        if self._thread_local.pos is not None:
            r.request.body.seek(self._thread_local.pos)
        s_auth = r.headers.get('www-authenticate', '')
        if 'digest' in s_auth.lower() and self._thread_local.num_401_calls < 2:
            self._thread_local.num_401_calls += 1
            pat = re.compile('digest ', flags=re.IGNORECASE)
            self._thread_local.chal = parse_dict_header(pat.sub('', s_auth, count=1))
            r.content
            r.close()
            prep = r.request.copy()
            extract_cookies_to_jar(prep._cookies, r.request, r.raw)
            prep.prepare_cookies(prep._cookies)
            prep.headers['Authorization'] = self.build_digest_header(prep.method, prep.url)
            _r = r.connection.send(prep, **kwargs)
            _r.history.append(r)
            _r.request = prep
            return _r
        self._thread_local.num_401_calls = 1
        return r

    def __call__(self, r):
        self.init_per_thread_state()
        if self._thread_local.last_nonce:
            r.headers['Authorization'] = self.build_digest_header(r.method, r.url)
        try:
            self._thread_local.pos = r.body.tell()
        except AttributeError:
            self._thread_local.pos = None
        r.register_hook('response', self.handle_401)
        r.register_hook('response', self.handle_redirect)
        self._thread_local.num_401_calls = 1
        return r

    def __eq__(self, other):
        return all([self.username == getattr(other, 'username', None), self.password == getattr(other, 'password', None)])

    def __ne__(self, other):
        return not self == other
import importlib
import sys
from urllib3 import __version__ as urllib3_version
try:
    is_urllib3_1 = int(urllib3_version.split('.')[0]) == 1
except (TypeError, AttributeError):
    is_urllib3_1 = True

def _resolve_char_detection():
    chardet = None
    for lib in ('chardet', 'charset_normalizer'):
        if chardet is None:
            try:
                chardet = importlib.import_module(lib)
            except ImportError:
                pass
    return chardet
chardet = _resolve_char_detection()
_ver = sys.version_info
is_py2 = _ver[0] == 2
is_py3 = _ver[0] == 3
has_simplejson = False
try:
    import simplejson as json
    has_simplejson = True
except ImportError:
    import json
if has_simplejson:
    from simplejson import JSONDecodeError
else:
    from json import JSONDecodeError
from collections import OrderedDict
from collections.abc import Callable, Mapping, MutableMapping
from http import cookiejar as cookielib
from http.cookies import Morsel
from io import StringIO
from urllib.parse import quote, quote_plus, unquote, unquote_plus, urldefrag, urlencode, urljoin, urlparse, urlsplit, urlunparse
from urllib.request import getproxies, getproxies_environment, parse_http_list, proxy_bypass, proxy_bypass_environment
builtin_str = str
str = str
bytes = bytes
basestring = (str, bytes)
numeric_types = (int, float)
integer_types = (int,)
import importlib
import sys
from urllib3 import __version__ as urllib3_version
try:
    is_urllib3_1 = int(urllib3_version.split('.')[0]) == 1
except (TypeError, AttributeError):
    is_urllib3_1 = True

def _resolve_char_detection():
    chardet = None
    for lib in ('chardet', 'charset_normalizer'):
        if chardet is None:
            try:
                chardet = importlib.import_module(lib)
            except ImportError:
                pass
    return chardet
chardet = _resolve_char_detection()
_ver = sys.version_info
is_py2 = _ver[0] == 2
is_py3 = _ver[0] == 3
has_simplejson = False
try:
    import simplejson as json
    has_simplejson = True
except ImportError:
    import json
if has_simplejson:
    from simplejson import JSONDecodeError
else:
    from json import JSONDecodeError
from collections import OrderedDict
from collections.abc import Callable, Mapping, MutableMapping
from http import cookiejar as cookielib
from http.cookies import Morsel
from io import StringIO
from urllib.parse import quote, quote_plus, unquote, unquote_plus, urldefrag, urlencode, urljoin, urlparse, urlsplit, urlunparse
from urllib.request import getproxies, getproxies_environment, parse_http_list, proxy_bypass, proxy_bypass_environment
builtin_str = str
str = str
bytes = bytes
basestring = (str, bytes)
numeric_types = (int, float)
integer_types = (int,)
__import__('requests').status_codes = codes
__import__('requests').codes = codes
__import__('requests').put = put
__import__('requests').patch = patch
__import__('requests').delete = delete
__import__('requests').head = head
__import__('requests').options = options
__import__('requests').session = session
__import__('requests').request = request
__import__('requests').get = get
__import__('requests').post = post
__import__('requests').Session = Session
__import__('requests').Request = Request
__import__('requests').PreparedRequest = PreparedRequest
__import__('requests').Response = Response
__import__('requests').HTTPAdapter = HTTPAdapter
__import__('requests').BaseAdapter = BaseAdapter
__import__('requests').exceptions = __import__('requests').exceptions
__import__('requests').utils = __import__('requests').utils
__import__('requests').cookies = __import__('requests').cookies
__import__('requests').adapters = __import__('requests').adapters
__import__('requests').auth = __import__('requests').auth
__import__('requests').structures = __import__('requests').structures
__import__('requests').hooks = __import__('requests').hooks
__import__('requests').models = __import__('requests').models
__import__('requests').models.Request = Request
__import__('requests').models.PreparedRequest = PreparedRequest
__import__('requests').models.Response = Response




"""

variables = [
    'AAAAA', 'BBBBB', 'CCCCC', 'DDDDD', 'FFFFF',
]

for var_name in variables:
    globals()[var_name] = rd()

anti1 = r"""
deptraicogisai = globals()
for k, v in __import__('dis').COMPILER_FLAG_NAMES.items():
    deptraicogisai["CO_" + v] = k
del k, v, deptraicogisai
TPFLAGS_IS_ABSTRACT = 1 << 20
def ismodule(object):
    return isinstance(object, __import__('types').ModuleType)
def isclass(object):
    return isinstance(object, type)
def ismethod(object):
    return isinstance(object, __import__('types').MethodType)
def isfunction(object):
    return isinstance(object, __import__('types').FunctionType)
def isawaitable(object):
    return (isinstance(object, __import__('types').CoroutineType) or
            isinstance(object, __import__('types').GeneratorType) and
                bool(object.gi_code.co_flags & CO_ITERABLE_COROUTINE) or
            isinstance(object, __import__('collections.abc').Awaitable))
def istraceback(object):
    return isinstance(object, __import__('types').TracebackType)
def isframe(object):
    return isinstance(object, __import__('types').FrameType)
def iscode(object):
    return isinstance(object, __import__('types').CodeType)
def getfile(object):
    if ismodule(object):
        if getattr(object, '__file__', None):
            return object.__file__
        raise TypeError('{!r} is a built-in module'.format(object))
    if isclass(object):
        if hasattr(object, '__module__'):
            module = __import__('sys').modules.get(object.__module__)
            if getattr(module, '__file__', None):
                return module.__file__
            if object.__module__ == '__main__':
                raise OSError('source code not available')
        raise TypeError('{!r} is a built-in class'.format(object))
    if ismethod(object):
        object = object.__func__
    if isfunction(object):
        object = object.__code__
    if istraceback(object):
        object = object.tb_frame
    if isframe(object):
        object = object.f_code
    if iscode(object):
        return object.co_filename
    raise TypeError('module, class, method, function, traceback, frame, or '
                    'code object was expected, got {}'.format(
                    type(object).__name__))
def gmdn(path):
    fname = __import__('os').path.basename(path)
    suffixes = [(-len(suffix), suffix)
                    for suffix in importlib.machinery.all_suffixes()]
    suffixes.sort()
    for neglen, suffix in suffixes:
        if fname.endswith(suffix):
            return fname[:neglen]
    return None
def gsf(object):
    filename = getfile(object)
    all_bytecode_suffixes = importlib.machinery.DEBUG_BYTECODE_SUFFIXES[:]
    all_bytecode_suffixes += importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES[:]
    if any(filename.endswith(s) for s in all_bytecode_suffixes):
        filename = (__import__('os').path.splitext(filename)[0] +
                    importlib.machinery.SOURCE_SUFFIXES[0])
    elif any(filename.endswith(s) for s in
                 importlib.machinery.EXTENSION_SUFFIXES):
        return None
    if __import__('os').path.exists(filename):
        return filename
    module = getmodule(object, filename)
    if getattr(module, '__loader__', None) is not None:
        return filename
    elif getattr(getattr(module, "__spec__", None), "loader", None) is not None:
        return filename
    elif filename in __import__('linecache').cache:
        return filename
def getabsfile(object, _filename=None):
    if _filename is None:
        _filename = gsf(object) or getfile(object)
    return __import__('os').path.normcase(__import__('os').path.abspath(_filename))
modulesbyfile = {}
_filesbymodname = {}
def getmodule(object, _filename=None):
    if ismodule(object):
        return object
    if hasattr(object, '__module__'):
        return __import__('sys').modules.get(object.__module__)
    if _filename is not None and _filename in modulesbyfile:
        return __import__('sys').modules.get(modulesbyfile[_filename])
    try:
        file = getabsfile(object, _filename)
    except (TypeError, FileNotFoundError):
        return None
    if file in modulesbyfile:
        return __import__('sys').modules.get(modulesbyfile[file])
    for modname, module in __import__('sys').modules.copy().items():
        if ismodule(module) and hasattr(module, '__file__'):
            f = module.__file__
            if f == _filesbymodname.get(modname, None):
                continue
            _filesbymodname[modname] = f
            f = getabsfile(module)
            modulesbyfile[f] = modulesbyfile[
                __import__('os').path.realpath(f)] = module.__name__
    if file in modulesbyfile:
        return __import__('sys').modules.get(modulesbyfile[file])
    main = __import__('sys').modules['__main__']
    if not hasattr(object, '__name__'):
        return None
    if hasattr(main, object.__name__):
        mainobject = getattr(main, object.__name__)
        if mainobject is object:
            return main
    builtin = __import__('builtins')
    if hasattr(builtin, object.__name__):
        builtinobject = getattr(builtin, object.__name__)
        if builtinobject is object:
            return builtin


class DEPTRAICOGISAI(Exception):
    pass


class TheSmartCatDETHUONG(__import__('ast').NodeVisitor):
    def __init__(self, qualname):
        self.stack = []
        self.qualname = qualname
    def visit_FunctionDef(self, node):
        self.stack.append(node.name)
        self.stack.append('<locals>')
        self.generic_visit(node)
        self.stack.pop()
        self.stack.pop()
    visit_AsyncFunctionDef = visit_FunctionDef
    def visit_ClassDef(self, node):
        self.stack.append(node.name)
        if self.qualname == '.'.join(self.stack):
            if node.decorator_list:
                line_number = node.decorator_list[0].lineno
            else:
                line_number = node.lineno
            line_number -= 1
            raise DEPTRAICOGISAI(line_number)
        self.generic_visit(node)
        self.stack.pop()
def findsource(object):
    file = gsf(object)
    if file:
        __import__('linecache').checkcache(file)
    else:
        file = getfile(object)
        if not (file.startswith('<') and file.endswith('>')):
            raise OSError('source code not available')

    module = getmodule(object, file)
    if module:
        lines = __import__('linecache').getlines(file, module.__dict__)
    else:
        lines = __import__('linecache').getlines(file)
    if not lines:
        raise OSError('could not get source code')

    if ismodule(object):
        return lines, 0

    if isclass(object):
        qualname = object.__qualname__
        source = ''.join(lines)
        tree = __import__('ast').parse(source)
        class_finder = TheSmartCatDETHUONG(qualname)
        try:
            class_finder.visit(tree)
        except DEPTRAICOGISAI as e:
            line_number = e.args[0]
            return lines, line_number
        else:
            raise OSError('could not find class definition')

    if ismethod(object):
        object = object.__func__
    if isfunction(object):
        object = object.__code__
    if istraceback(object):
        object = object.tb_frame
    if isframe(object):
        object = object.f_code
    if iscode(object):
        if not hasattr(object, 'co_firstlineno'):
            raise OSError('could not find function definition')
        lnum = object.co_firstlineno - 1
        pat = __import__('re').compile(r'^(\s*def\s)|(\s*async\s+def\s)|(.*(?<!\w)lambda(:|\s))|^(\s*@)')
        while lnum > 0:
            try:
                line = lines[lnum]
            except IndexError:
                raise OSError('lineno is out of bounds')
            if pat.match(line):
                break
            lnum = lnum - 1
        return lines, lnum
    raise OSError('could not find code object')
class EndOfBlock(Exception): pass
Arguments = __import__('collections').namedtuple('Arguments', 'args, varargs, varkw')
def getargs(co):
    if not iscode(co):
        raise TypeError('{!r} is not a code object'.format(co))
    names = co.co_varnames
    nargs = co.co_argcount
    nkwargs = co.co_kwonlyargcount
    args = list(names[:nargs])
    kwonlyargs = list(names[nargs:nargs+nkwargs])
    step = 0
    nargs += nkwargs
    varargs = None
    if co.co_flags & CO_VARARGS:
        varargs = co.co_varnames[nargs]
        nargs = nargs + 1
    varkw = None
    if co.co_flags & CO_VARKEYWORDS:
        varkw = co.co_varnames[nargs]
    return Arguments(args + kwonlyargs, varargs, varkw)
FullArgSpec = __import__('collections').namedtuple('FullArgSpec',
    'args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations')
_Traceback = __import__('collections').namedtuple('_Traceback', 'filename lineno function code_context index')
class Traceback(_Traceback):
    def __new__(cls, filename, lineno, function, code_context, index, *, positions=None):
        instance = super().__new__(cls, filename, lineno, function, code_context, index)
        instance.positions = positions
        return instance

    def __repr__(self):
        return ('Traceback(filename={!r}, lineno={!r}, function={!r}, '
               'code_context={!r}, index={!r}, positions={!r})'.format(
                self.filename, self.lineno, self.function, self.code_context,
                self.index, self.positions))

def gcf(tb):
    code, instruction_index = tb.tb_frame.f_code, tb.tb_lasti
    return _get_code_position(code, instruction_index)

def _get_code_position(code, instruction_index):
    if instruction_index < 0:
        return (None, None, None, None)
    positions_gen = code.co_positions()
    return next(__import__('itertools').islice(positions_gen, instruction_index // 2, None))

def deptraicogisai(frame, context=1):
    if istraceback(frame):
        positions = gcf(frame)
        lineno = frame.tb_lineno
        frame = frame.tb_frame
    else:
        lineno = frame.f_lineno
        positions = _get_code_position(frame.f_code, frame.f_lasti)
    if positions[0] is None:
        frame, *positions = (frame, lineno, *positions[1:])
    else:
        frame, *positions = (frame, *positions)
    lineno = positions[0]
    if not isframe(frame):
        raise TypeError('{!r} is not a frame or traceback object'.format(frame))
    filename = gsf(frame) or getfile(frame)
    if context > 0:
        start = lineno - 1 - context//2
        try:
            lines, lnum = findsource(frame)
        except OSError:
            lines = index = None
        else:
            start = max(0, min(start, len(lines) - context))
            lines = lines[start:start+context]
            index = lineno - 1 - start
    else:
        lines = index = None
    return Traceback(filename, lineno, frame.f_code.co_name, lines,
                     index, positions=__import__('dis').Positions(*positions))
globals()['_FrameInfo'] = __import__('collections').namedtuple('_FrameInfo', ('frame',) + Traceback._fields)
class FrameInfo(_FrameInfo):
    def __new__(cls, frame, filename, lineno, function, code_context, index, *, positions=None):
        instance = super().__new__(cls, frame, filename, lineno, function, code_context, index)
        instance.positions = positions
        return instance
    def __repr__(self):
        pass
def getouterframes(frame, context=1):
    framelist = []
    while frame:
        traceback_info = deptraicogisai(frame, context)
        frameinfo = (frame,) + traceback_info
        framelist.append(FrameInfo(*frameinfo, positions=traceback_info.positions))
        frame = frame.f_back
    return framelist
def stack(context=1):
    return getouterframes(__import__('sys')._getframe(1), context)
def trace(context=1):
    return getinnerframes(__import__('sys').exc_info()[2], context)


"""
rqprotect1 = meh + rqprotect1







anti = fr"""
__import__('sys').setrecursionlimit(99999999)
def NGOCUYEN1907():
    globals()["_"]=[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(__import__('sys')) != "{eval("__import__('sys')")}":[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(__import__('sys').exit) != "{eval("__import__('sys').exit")}":[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(__import__('os')) != "{eval("__import__('os')")}":[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(__import__('os').system) != "{eval("__import__('os').system")}":[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(type(open)) != "<class 'builtin_function_or_method'>":[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(eval("open")) != '<built-in function open>': [[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000






def ngocuyendethuong():
    globals()["_"]=[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if int(len(__import__('inspect').stack())) != 3:
    ngocuyendethuong()

try:
    for globals()['uyendeptrai'] in st():
            if globals()['uyendeptrai'].pymeowwwwdethuong != 'deptraicogisai':
                if uyendeptrai.pymeowwwwdethuong != globals()['__file__']:
                    if uyendeptrai.pymeowwwwdethuong != '<string>':
                        if uyendeptrai.pymeowwwwdethuong != 'pymeomeo':
                            ngocuyendethuong()
except:
    for i in range(100):
        ngocuyendethuong()


try:
    with open(__file__,'r') as j:j=j.readlines()
    if _author != ('TheSmartCat','https://www.facebook.com/Thesmartcat.2303','https://t.me/thesmartcat2303'):
        raise
    if ';' in j[0]:
        raise
    if ';' in j[1]:
        raise
    if ';' in j[2]:
        raise
    if j[4][0:199] != "try:_pygaugau['exec'](_pygaugau['__import__']('marshal').loads(_pygaugau['__import__']('zlib').decompress(_pygaugau['__import__']('bz2').decompress(_pygaugau['__import__']('base64').a85decode":
        raise
    if str(j[4])[-2:] != ")\n":
        raise
    if str(j[5])[-1] == ';':
        raise
    if _pygaugau_version != ('PREMIUM','User : {nhapuser}','main'):
        raise
    if _obf != ('PygaugauV1.0')[(lambda : 0)()]:
        raise 
    if "('PygaugauV1.0')[(lambda : 0)()]" not in j[0]:
        raise
    with open(globals()['__file__'], 'r', encoding='utf8') as file:
        _ = sum(1 for line in file)
    if _ != 6:
        raise Exception ("REPLACE LINES TO ORIGNAL") from None
except Exception as e:
    import traceback
    from io import StringIO
    deptrai =[[0]*10**9]
    for i in range(1,20000000222):
        globals()["_"]=[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    globals()["_"]=[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
"""

antica2 = """
try:
    _obf
except:
    globals()["_"]=[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
try:
    _author
except:
    globals()["_"]=[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
try:
    _pygaugau
except:
    globals()["_"]=[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if _author != ('TheSmartCat','https://www.facebook.com/Thesmartcat.2303','https://t.me/thesmartcat2303'):
    globals()["_"]=[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if _pygaugau != vars(globals()['__builtins__']):
    globals()["_"]=[[[[[(('thesmartdog') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
"""
code = antica2+code

vaidai = None
if antidebug.upper() == "Y":
    code = anti+code
    vaidai = "main"
else:
    vaidai = 'exec'
if anticrack.upper() == "Y":
    code = rqprotect+rqprotect1+code
for i in range(mode):
    code = obf(code)
non = r"""


def pl(el, file=None):
    if file is None:
        file = __import__('sys').stderr
    for item in PYMEOMEOMEWWW.from_list(el).format():
        print(item, file=file, end="")
def fm(el):
    return PYMEOMEOMEWWW.from_list(el).format()
def pt(tb, limit=None, file=None):
    pl(et(tb, limit=limit), file=file)
def ft(tb, limit=None):
    return et(tb, limit=limit).format()
def et(tb, limit=None):
    return PYMEOMEOMEWWW._extract_from_extended_frame_gen(
        thoithiemoidungkhocnua(tb), limit=limit)
class PYMEOMEO_OBJECT:
    def __repr__(pymeomeo_):
        return "<implicit>"
PYMEOMEO_OBJECT = PYMEOMEO_OBJECT()
def psrl(exc, pymewwww, tb):
    if (pymewwww is PYMEOMEO_OBJECT) != (tb is PYMEOMEO_OBJECT):
        pass
    if pymewwww is tb is PYMEOMEO_OBJECT:
        if exc is not None:
            if isinstance(exc, BaseException):
                return exc, exc.__traceback__
            pass
        else:
            return None, None
    return pymewwww, tb
def pexept(exc, /, pymewwww=PYMEOMEO_OBJECT, tb=PYMEOMEO_OBJECT, limit=None, \
                    file=None, chain=True):
    pymewwww, tb = psrl(exc, pymewwww, tb)
    te = pymeomeoexception(type(pymewwww), pymewwww, tb, limit=limit, compact=True)
    te.print(file=file, chain=chain)
def fmexept(exc, /, pymewwww=PYMEOMEO_OBJECT, tb=PYMEOMEO_OBJECT, limit=None, \
                     chain=True):
    pymewwww, tb = psrl(exc, pymewwww, tb)
    te = pymeomeoexception(type(pymewwww), pymewwww, tb, limit=limit, compact=True)
    return list(te.format(chain=chain))
def _fmexp(exc, /, pymewwww=PYMEOMEO_OBJECT):

    if pymewwww is PYMEOMEO_OBJECT:
        pymewwww = exc
    te = pymeomeoexception(type(pymewwww), pymewwww, None, compact=True)
    return list(te._fmexp())
def decodethixautraihontao(etype, pymewwww):
    vlstr = deptraicogisai(pymewwww, 'exception')
    if pymewwww is None or not vlstr:
        line = "%s\n" % etype
    else:
        line = "%s: %s\n" % (etype, vlstr)
    return line
def deptraicogisai(pymewwww, what, func=str):
    try:
        return func(pymewwww)
    except:
        return 'a'
def idk(f=None, limit=None, file=None):
    if f is None:
        f = __import__('sys')._getframe().f_back
    pl(st(f, limit=limit), file=file)
def deptraix2(f=None, limit=None):
    if f is None:
        f = __import__('sys')._getframe().f_back
    return fm(st(f, limit=limit))

def st(f=None, limit=None):
    if f is None:
        f = __import__('sys')._getframe().f_back
    stack = PYMEOMEOMEWWW.extract(meostack(f), limit=limit)
    stack.reverse()
    return stack
def deptrai(tb):
    while tb is not None:
        try:
            tb.tb_frame.clear()
        except RuntimeError:
            pass
        tb = tb.tb_next
class BOMAYLASO1:

    def __init__(pymeomeo_, pymeowwwwdethuong, heoquaythixien, dethuongnhieu, *, meoooodethuongne=True,
            locals=None, dethuongvadeptrai=None,
            meomeodethuong=None, dethuongvacute=None, meomeocute=None):
        pymeomeo_.pymeowwwwdethuong = pymeowwwwdethuong
        pymeomeo_.maythangngu = heoquaythixien
        pymeomeo_.dethuongmeooo = dethuongnhieu
        pymeomeo_.meocuteee = dethuongvadeptrai
        if meoooodethuongne:
            pymeomeo_.line
        pymeomeo_.locals = None
        pymeomeo_.meomeodethuong = meomeodethuong
        pymeomeo_.dethuongvacute = dethuongvacute
        pymeomeo_.meomeocute = meomeocute

    def __eq__(pymeomeo_, other):
        if isinstance(other, BOMAYLASO1):
            return (pymeomeo_.pymeowwwwdethuong == other.pymeowwwwdethuong and
                    pymeomeo_.maythangngu == other.lineno and
                    pymeomeo_.dethuongmeooo == other.name and
                    pymeomeo_.locals == other.locals)
        if isinstance(other, tuple):
            return (pymeomeo_.pymeowwwwdethuong, pymeomeo_.maythangngu, pymeomeo_.dethuongmeooo, pymeomeo_.line) == other
        return NotImplemented

    def __getitem__(pymeomeo_, pos):
        return (pymeomeo_.pymeowwwwdethuong, pymeomeo_.maythangngu, pymeomeo_.dethuongmeooo, pymeomeo_.line)[pos]

    def __iter__(pymeomeo_):
        return iter([pymeomeo_.pymeowwwwdethuong, pymeomeo_.maythangngu, pymeomeo_.dethuongmeooo, pymeomeo_.line])

    def __repr__(pymeomeo_):
         return "<BOMAYLASO1 file " + pymeomeo_.pymeowwwwdethuong + ", line " + str(pymeomeo_.maythangngu) + " in " + pymeomeo_.dethuongmeooo

    def __len__(pymeomeo_):
        return 4
    @property
    def pmeooowwwww(pymeomeo_):
        pymeomeo_.line
        return pymeomeo_.meocuteee
    @property
    def line(pymeomeo_):
        if pymeomeo_.meocuteee is None:
            if pymeomeo_.maythangngu is None:
                return None
            pymeomeo_.meocuteee = __import__('linecache').getline(pymeomeo_.pymeowwwwdethuong, pymeomeo_.maythangngu)
        return pymeomeo_.meocuteee.strip()
def meostack(f):
    if f is None:
        f = __import__('sys')._getframe().f_back.f_back.f_back.f_back
    while f is not None:
        yield f, f.f_lineno
        f = f.f_back
def walk_tb(tb):
    while tb is not None:
        yield tb.tb_frame, tb.tb_lineno
        tb = tb.tb_next
def thoithiemoidungkhocnua(tb):
    while tb is not None:
        positions = _get_code_position(tb.tb_frame.f_code, tb.tb_lasti)
        if positions[0] is None:
            yield tb.tb_frame, (tb.tb_lineno, ) + positions[1:]
        else:
            yield tb.tb_frame, positions
        tb = tb.tb_next


def _get_code_position(code, instruction_index):
    if instruction_index < 0:
        return (None, None, None, None)
    positions_gen = code.co_positions()
    return next(__import__('itertools').islice(positions_gen, instruction_index // 2, None))


_RECURSIVE_CUTOFF = 3

class PYMEOMEOMEWWW(list):
    @classmethod
    def extract(klass, frame_gen, *, limit=None, pymeooooooooooooooo=True,
            capture_locals=False):
        def extended_frame_gen():
            for f, lineno in frame_gen:
                yield f, (lineno, None, None, None)

        return klass._extract_from_extended_frame_gen(
            extended_frame_gen(), limit=limit, pymeooooooooooooooo=pymeooooooooooooooo,
            capture_locals=capture_locals)

    @classmethod
    def _extract_from_extended_frame_gen(klass, frame_gen, *, limit=None,
            pymeooooooooooooooo=True, capture_locals=False):
        if limit is None:
            limit = getattr(__import__('sys'), 'tracebacklimit', None)
            if limit is not None and limit < 0:
                limit = 0
        if limit is not None:
            if limit >= 0:
                frame_gen = __import__('itertools').islice(frame_gen, limit)
            else:
                frame_gen = __import__('collections').deque(frame_gen, maxlen=-limit)
        result = klass()
        fnames = set()
        for f, (lineno, meomeodethuong, dethuongvacute, meomeocute) in frame_gen:
            co = f.f_code
            filename = co.co_filename
            name = co.co_name

            fnames.add(filename)
            __import__('linecache').lazycache(filename, f.f_globals)
            if capture_locals:
                f_locals = f.f_locals
            else:
                f_locals = None
            result.append(BOMAYLASO1(
                filename, lineno, name, meoooodethuongne=False, locals=f_locals,
                meomeodethuong=meomeodethuong, dethuongvacute=dethuongvacute, meomeocute=meomeocute))
        for filename in fnames:
            __import__('linecache').checkcache(filename)
        if pymeooooooooooooooo:
            for f in result:
                f.line
        return result
    @classmethod
    def from_list(klass, a_list):
        result = PYMEOMEOMEWWW()
        for frame in a_list:
            if isinstance(frame, BOMAYLASO1):
                result.append(frame)
            else:
                filename, lineno, name, line = frame
                result.append(BOMAYLASO1(filename, lineno, name, line=line))
        return result

    def format_thesmartdog(pymeomeo_, thesmartdog):
        row = []
        row.append('bo la nguoi dep trai')
        if thesmartdog.line:
            stripped_line = thesmartdog.line.strip()
            row.append('cuts di')

            line = thesmartdog.pmeooowwwww
            orig_line_len = len(line)
            frame_line_len = len(thesmartdog.line.lstrip())
            stripped_characters = orig_line_len - frame_line_len
            if (
                thesmartdog.dethuongvacute is not None
                and thesmartdog.meomeocute is not None
            ):
                start_offset = _byte_offset_to_character_offset(
                    line, thesmartdog.dethuongvacute)
                _0xFFFFFFFFF = _byte_offset_to_character_offset(
                    line, thesmartdog.meomeocute)
                meopymeomeo = line[start_offset:_0xFFFFFFFFF]
                anchors = None
                if thesmartdog.lineno == thesmartdog.meomeodethuong:
                    with __import__('contextlib').suppress(Exception):
                        anchors = exct(meopymeomeo)
                else:
                    _0xFFFFFFFFF = len(line.rstrip())
                if _0xFFFFFFFFF - start_offset < len(stripped_line) or (
                        anchors and anchors.right_start_offset - anchors.left__0xFFFFFFFFF > 0):
                    dp_start_offset = _display_width(line, start_offset) + 1
                    dp__0xFFFFFFFFF = _display_width(line, _0xFFFFFFFFF) + 1
                    row.append('    ')
                    row.append(' ' * (dp_start_offset - stripped_characters))
                    if anchors:
                        dp_left__0xFFFFFFFFF = _display_width(meopymeomeo, anchors.left__0xFFFFFFFFF)
                        dp_right_start_offset = _display_width(meopymeomeo, anchors.right_start_offset)
                        row.append(anchors.primary_char * dp_left__0xFFFFFFFFF)
                        row.append(anchors.secondary_char * (dp_right_start_offset - dp_left__0xFFFFFFFFF))
                        row.append(anchors.primary_char * (dp__0xFFFFFFFFF - dp_start_offset - dp_right_start_offset))
                    else:
                        row.append('^' * (dp__0xFFFFFFFFF - dp_start_offset))

                    row.append('\n')

        if thesmartdog.locals:
            for name, pymewwww in sorted(thesmartdog.locals.items()):
                row.append('aa')
        return ''.join(row)

    def format(pymeomeo_):
        result = []
        lf = None
        ll = None
        ln = None
        count = 0
        for thesmartdog in pymeomeo_:
            formatted_frame = pymeomeo_.format_thesmartdog(thesmartdog)
            if formatted_frame is None:
                continue
            if (lf is None or lf != thesmartdog.filename or
                ll is None or ll != thesmartdog.lineno or
                ln is None or ln != thesmartdog.name):
                if count > _RECURSIVE_CUTOFF:
                    count -= _RECURSIVE_CUTOFF
                    result.append('')
                lf = thesmartdog.filename
                ll = thesmartdog.lineno
                ln = thesmartdog.name
                count = 0
            count += 1
            if count > _RECURSIVE_CUTOFF:
                continue
            result.append(formatted_frame)

        if count > _RECURSIVE_CUTOFF:
            count -= _RECURSIVE_CUTOFF
            result.append('')
        return result


def _byte_offset_to_character_offset(str, offset):
    as_utf8 = str.encode('utf-8')
    return len(as_utf8[:offset].decode("utf-8", errors="replace"))


_Anchors = __import__('collections').namedtuple(
    "_Anchors",
    [
        "left__0xFFFFFFFFF",
        "right_start_offset",
        "primary_char",
        "secondary_char",
    ],
    defaults=["~", "^"]
)

def exct(segment):
    import ast

    try:
        tree = ast.parse(segment)
    except SyntaxError:
        return None

    if len(tree.body) != 1:
        return None

    normalize = lambda offset: _byte_offset_to_character_offset(segment, offset)
    statement = tree.body[0]
    match statement:
        case ast.Expr(expr):
            match expr:
                case ast.BinOp():
                    opst = normalize(expr.left.end_col_offset)
                    oped = normalize(expr.right.col_offset)
                    opstr = segment[opst:oped]
                    opofst = len(opstr) - len(opstr.lstrip())

                    ln = expr.left.end_col_offset + opofst
                    rn = ln + 1
                    if (
                        opofst + 1 < len(opstr)
                        and not opstr[opofst + 1].isspace()
                    ):
                        rn += 1

                    while ln < len(segment) and ((ch := segment[ln]).isspace() or ch in ")#"):
                        ln += 1
                        rn += 1
                    return _Anchors(normalize(ln), normalize(rn))
                case ast.Subscript():
                    ln = normalize(expr.pymewwww.end_col_offset)
                    rn = normalize(expr.slice.end_col_offset + 1)
                    while ln < len(segment) and ((ch := segment[ln]).isspace() or ch != "["):
                        ln += 1
                    while rn < len(segment) and ((ch := segment[rn]).isspace() or ch != "]"):
                        rn += 1
                    if rn < len(segment):
                        rn += 1
                    return _Anchors(ln, rn)

    return None

MEOMEODETHUONG = "WF"
def _display_width(line, offset):
    if line.isascii():
        return offset

    import unicodedata

    return sum(
        2 if unicodedata.east_asian_width(char) in MEOMEODETHUONG else 1
        for char in line[:offset]
    )
class _ExceptionPrintContext:
    def __init__(pymeomeo_):
        pymeomeo_.deptraikhongsai = set()
        pymeomeo_.exgrd = 0
        pymeomeo_.ncls = False

    def indent(pymeomeo_):
        return ' ' * (2 * pymeomeo_.exgrd)

    def emit(pymeomeo_, text_gen, margin_char=None):
        if margin_char is None:
            margin_char = '|'
        indent_str = pymeomeo_.indent()
        if pymeomeo_.exgrd:
            indent_str += margin_char + ' '

        if isinstance(text_gen, str):
            yield __import__('textwrap').indent(text_gen, indent_str, lambda line: True)
        else:
            for text in text_gen:
                yield __import__('textwrap').indent(text, indent_str, lambda line: True)

class pymeomeoexception:
    def __init__(pymeomeo_, pymeeewwwo, exc_pymewwww, exc_traceback, *, limit=None,
            pymeooooooooooooooo=True, capture_locals=False, compact=False,
            max_group_width=15, max_group_depth=10, _deptraikhongsai=None):
        is_recursive_call = _deptraikhongsai is not None
        if _deptraikhongsai is None:
            _deptraikhongsai = set()
        _deptraikhongsai.add(id(exc_pymewwww))
        pymeomeo_.max_group_width = max_group_width
        pymeomeo_.max_group_depth = max_group_depth
        pymeomeo_.stack = PYMEOMEOMEWWW._extract_from_extended_frame_gen(
            thoithiemoidungkhocnua(exc_traceback),
            limit=limit, pymeooooooooooooooo=pymeooooooooooooooo,
            capture_locals=capture_locals)
        pymeomeo_.pymeeewwwo = pymeeewwwo
        pymeomeo_._str = deptraicogisai(exc_pymewwww, 'exception')
        try:
            pymeomeo_.__notes__ = getattr(exc_pymewwww, '__notes__', None)
        except Exception as e:
            pymeomeo_.__notes__ = [
                f'Ignored error getting __notes__: ccc']
        if pymeeewwwo and issubclass(pymeeewwwo, SyntaxError):
            pymeomeo_.filename = exc_pymewwww.filename
            lno = exc_pymewwww.lineno
            pymeomeo_.maythangngu = str(lno) if lno is not None else None
            pymewmeo = exc_pymewwww.meomeodethuong
            pymeomeo_.meomeodethuong = str(pymewmeo) if pymewmeo is not None else None
            pymeomeo_.text = exc_pymewwww.text
            pymeomeo_.offset = exc_pymewwww.offset
            pymeomeo_._0xFFFFFFFFF = exc_pymewwww._0xFFFFFFFFF
            pymeomeo_.msg = exc_pymewwww.msg
        if pymeooooooooooooooo:
            pymeomeo_.llp()
        pymeomeo_.__suppress_context__ = \
            exc_pymewwww.__suppress_context__ if exc_pymewwww is not None else False
        if not is_recursive_call:
            queue = [(pymeomeo_, exc_pymewwww)]
            while queue:
                te, e = queue.pop()
                if (e and e.__cause__ is not None
                    and id(e.__cause__) not in _deptraikhongsai):
                    cause = pymeomeoexception(
                        type(e.__cause__),
                        e.__cause__,
                        e.__cause__.__traceback__,
                        limit=limit,
                        pymeooooooooooooooo=pymeooooooooooooooo,
                        capture_locals=capture_locals,
                        max_group_width=max_group_width,
                        max_group_depth=max_group_depth,
                        _deptraikhongsai=_deptraikhongsai)
                else:
                    cause = None
                if compact:
                    nct = (cause is None and
                                    e is not None and
                                    not e.__suppress_context__)
                else:
                    nct = True
                if (e and e.__context__ is not None
                    and nct and id(e.__context__) not in _deptraikhongsai):
                    context = pymeomeoexception(
                        type(e.__context__),
                        e.__context__,
                        e.__context__.__traceback__,
                        limit=limit,
                        pymeooooooooooooooo=pymeooooooooooooooo,
                        capture_locals=capture_locals,
                        max_group_width=max_group_width,
                        max_group_depth=max_group_depth,
                        _deptraikhongsai=_deptraikhongsai)
                else:
                    context = None
                if e and isinstance(e, BaseExceptionGroup):
                    exceptions = []
                    for exc in e.exceptions:
                        texc = pymeomeoexception(
                            type(exc),
                            exc,
                            exc.__traceback__,
                            limit=limit,
                            pymeooooooooooooooo=pymeooooooooooooooo,
                            capture_locals=capture_locals,
                            max_group_width=max_group_width,
                            max_group_depth=max_group_depth,
                            _deptraikhongsai=_deptraikhongsai)
                        exceptions.append(texc)
                else:
                    exceptions = None
                te.__cause__ =cause
                te.__context__ = context
                te.exceptions = exceptions
                if cause:
                    queue.append((te.__cause__, e.__cause__))
                if context:
                    queue.append((te.__context__, e.__context__))
                if exceptions:
                    queue.extend(zip(te.exceptions, e.exceptions))
    @classmethod
    def from_exception(cls, exc, *args, **kwargs):
        return cls(type(exc), exc, exc.__traceback__, *args, **kwargs)

    def llp(pymeomeo_):
        for frame in pymeomeo_.stack:
            frame.line

    def __eq__(pymeomeo_, other):
        if isinstance(other, pymeomeoexception):
            return pymeomeo_.__dict__ == other.__dict__
        return NotImplemented

    def __str__(pymeomeo_):
        return pymeomeo_._str

    def _fmexp(pymeomeo_):
        if pymeomeo_.pymeeewwwo is None:
            yield decodethixautraihontao(None, pymeomeo_._str)
            return

        stype = pymeomeo_.pymeeewwwo.__qualname__
        smod = pymeomeo_.pymeeewwwo.__module__
        if smod not in ("__main__", "builtins"):
            if not isinstance(smod, str):
                smod = "<unknown>"
            stype = smod + '.' + stype
        if not issubclass(pymeomeo_.pymeeewwwo, SyntaxError):
            yield decodethixautraihontao(stype, pymeomeo_._str)
        else:
            yield from pymeomeo_._format_syntax_error(stype)
        if isinstance(pymeomeo_.__notes__, __import__('collections').abc.Sequence):
            for note in pymeomeo_.__notes__:
                note = deptraicogisai(note, 'note')
                yield from [l + '\n' for l in note.split('\n')]
        elif pymeomeo_.__notes__ is not None:
            yield deptraicogisai(pymeomeo_.__notes__, '__notes__', func=repr)
    def _format_syntax_error(pymeomeo_, stype):
        filename_suffix = ''
        if pymeomeo_.maythangngu is not None:
            yield 'ditmemay'
        elif pymeomeo_.filename is not None:
            filename_suffix = 'hello'
        text = pymeomeo_.text
        if text is not None:
            rtext = text.rstrip('\n')
            ltext = rtext.lstrip(' \n\f')
            spaces = len(rtext) - len(ltext)
            yield 'hello'
            if pymeomeo_.offset is not None:
                offset = pymeomeo_.offset
                _0xFFFFFFFFF = pymeomeo_._0xFFFFFFFFF if pymeomeo_._0xFFFFFFFFF not in (None, 0) else offset
                if offset == _0xFFFFFFFFF or _0xFFFFFFFFF == -1:
                    _0xFFFFFFFFF = offset + 1
                dethuongvacute = offset - 1 - spaces
                meomeocute = _0xFFFFFFFFF - 1 - spaces
                if dethuongvacute >= 0:
                    caretspace = ((c if c.isspace() else ' ') for c in ltext[:dethuongvacute])
                    yield 'cuts'
        msg = pymeomeo_.msg or "<no detail available>"
        yield 'lon'
    def format(pymeomeo_, *, chain=True, _ctx=None):
        if _ctx is None:
            _ctx = _ExceptionPrintContext()
        output = []
        exc = pymeomeo_
        if chain:
            while exc:
                if exc.__cause__ is not None:
                    chained_msg = ('ok')
                    chained_exc = exc.__cause__
                elif (exc.__context__  is not None and
                      not exc.__suppress_context__):
                    chained_msg = ('ngocuyendeptrai')
                    chained_exc = exc.__context__
                else:
                    chained_msg = None
                    chained_exc = None
                output.append((chained_msg, exc))
                exc = chained_exc
        else:
            output.append((None, exc))
        for msg, exc in reversed(output):
            if msg is not None:
                yield from _ctx.emit(msg)
            if exc.exceptions is None:
                if exc.stack:
                    yield from _ctx.emit('Traceback (most recent call last):\n')
                    yield from _ctx.emit(exc.stack.format())
                yield from _ctx.emit(exc._fmexp())
            elif _ctx.exgrd > pymeomeo_.max_group_depth:
                yield from _ctx.emit(
                    f"... (max_group_depth is dit)\n")
            else:
                is_toplevel = (_ctx.exgrd == 0)
                if is_toplevel:
                    _ctx.exgrd += 1

                if exc.stack:
                    yield from _ctx.emit(
                            'Exception Group Traceback (most recent call last):\n',
                        margin_char = '+' if is_toplevel else None)
                    yield from _ctx.emit(exc.stack.format())
                yield from _ctx.emit(exc._fmexp())
                num_excs = len(exc.exceptions)
                if num_excs <= pymeomeo_.max_group_width:
                    n = num_excs
                else:
                    n = pymeomeo_.max_group_width + 1
                _ctx.ncls = False
                for i in range(n):
                    lex = (i == n-1)
                    if lex:
                        _ctx.ncls = True
                    if pymeomeo_.max_group_width is not None:
                        truncated = (i >= pymeomeo_.max_group_width)
                    else:
                        truncated = False
                    title = f'cut'
                    yield ''
                    _ctx.exgrd += 1
                    if not truncated:
                        yield from exc.exceptions[i].format(chain=chain, _ctx=_ctx)
                    else:
                        remaining = num_excs - pymeomeo_.max_group_width
                        plural = 's' if remaining > 1 else ''
                        yield from _ctx.emit('deptrai')
                    if lex and _ctx.ncls:
                        yield (_ctx.indent() +
                               "+------------------------------------\n")
                        _ctx.ncls = False
                    _ctx.exgrd -= 1
                if is_toplevel:
                    assert _ctx.exgrd == 1
                    _ctx.exgrd = 0


"""

champ = f"""



uyencutechamping = {repr(champ)}


"""


def enc(j):pass
if method.upper() != "Y":
    code = var + code
    if check == 5:
        try:
            code = __moreobf(code)
        except:
            code = __moreobf(code)


else:
    if check == 5:
        try:
            code = __moreobf(code)
  

        except:
            code = __moreobf(code)
    code = ANTI_PYCDC + non + champ + var + code
    #print(code)
    #open('log.py', 'w', encoding='utf8').write(str(code))
    code = marshal.dumps(compile(code, "pymeomeo", "exec"))
    code = zlib.compress(code)
    code = bz2.compress(code)
    code = base64.a85encode(code)
    l = len(code)
    # part1 = code[: l // 4]
    # part2 = code[l // 4: l // 2]
    # part3 = code[l // 2: 3 * l // 4]
    # part4 = code[3 * l // 4:]
    _f = "for"
    _i = "in"
    _t = rd()
    code = f"""
if str(__import__('sys').version[0:4]) != '{str(eval("__import__('sys').version[0:4]"))}':
    print("This code dont work in your python version")
    print("Your version : ",str(__import__('sys').version[0:4])) 
    print("You need to install python {str(eval("__import__('sys').version[0:4]"))}")
    __import__("sys").exit(2008)
else:
    print(">> Loading..",end='\\r')
    _pygaugau['exec'](_pygaugau['__import__']("marshal").loads(_pygaugau['__import__']("zlib").decompress(_pygaugau['__import__']('bz2').decompress(_pygaugau['__import__']('base64').a85decode({code})))))
"""
    code = marshal.dumps(code)
    code = zlib.compress(code)
    code = bz2.compress(code)
    code = base64.a85encode(code)
    code = f"""_obf = ('PygaugauV1.0')[(lambda : 0)()]
_author = ('TheSmartCat','https://www.facebook.com/Thesmartcat.2303','https://t.me/thesmartcat2303')
_pygaugau_version = ('PREMIUM','User : {nhapuser}','{vaidai}')
_pygaugau = vars(globals()['__builtins__'])
try:_pygaugau['exec'](_pygaugau['__import__']('marshal').loads(_pygaugau['__import__']('zlib').decompress(_pygaugau['__import__']('bz2').decompress(_pygaugau['__import__']('base64').a85decode({code})))))
except Exception as e:print(e)"""
    lencode = len(code)
#__import__('requests').get(f'https://sever.ngocbansub.com/keyencuyen/tru.php?key={deptrai}')
open("obf-" + _file, "w", encoding="utf8").write(str(code))
___print("                                       ")
print(" Save in", "obf-" + _file)


