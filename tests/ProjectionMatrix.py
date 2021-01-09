"""
This file just contains some info about the OpenGL
Projection Matrix (used by Unity and Blender) as reference

Unity Projection Matrix:
(x  0  a  0)    x = 2 * n / (r - l)         y = 2 * n / (t - b)
(0  y  b  0)    a = (r + l) / (r - l)       b = (t + b) / (t - b)
(0  0  c  d)    c = -(f + n) / (f - n)      d = -(2 * f * n) / (f - n)
(0  0  e  0)    e = -1

r = right, l = left, n = near, f = far, t = top, b = bot

[ 2 * n / (r - l) ,        0        , (r + l) / (r - l)   ,             0           ]
[       0         , 2 * n / (t - b) , (t + b) / (t - b)   ,             0           ]
[       0         ,        0        , -(f + n) / (f - n)  , -(2 * f * n) / (f - n)  ]
[       0         ,        0        ,          -1         ,             0           ]

sample unity matrix:
"e00":3.2344205379486086,   "e01":0.0,              "e02":-0.01493251882493496, "e03":0.0,
"e10":0.0,                  "e11":1.492809534072876,"e12":0.001684027025476098, "e13":0.0,
"e20":0.0,                  "e21":0.0,              "e22":-1.0100502967834473,  "e23":-0.2010050266981125,
"e30":0.0,                  "e31":0.0,              "e32":-1.0,                 "e33":0.0

( scale ,    0      ,       offset        ,     0       ,   )
(   0   ,   scale   ,       offset        ,     0       ,   )
(   0   ,   0       ,  depth (scales Z)   , depth (const),  )
(   0   ,   0       ,     perspective     ,     0    ,      )

offset (linear) -> (incomming)X * x + a * Z (the more shift, the more objs far Z are shifted)
+a = shift right || -a = shift left


sample blender matrix (default scene):
// no lens shift
<Matrix 4x4 (2.7778, 0.0000,  0.0000,  0.0000)
            (0.0000, 4.9383,  0.0000,  0.0000)
            (0.0000, 0.0000, -1.0020, -0.2002)
            (0.0000, 0.0000, -1.0000,  0.0000)>


"""