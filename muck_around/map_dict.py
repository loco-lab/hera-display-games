import numpy as np

led_map = {
    np.array([0,0]):10,
    np.array([1,0]):9,
    np.array([2,0]):8,
    np.array([3,0]):7,
    np.array([4,0]):6,
    np.array([5,0]):5,
    np.array([6,0]):4,
    np.array([7,0]):3,
    np.array([8,0]):2,
    np.array([9,0]):1,
    np.array([10,0]):0,
    np.array([11,0]):'dead',

    np.array([0,1]):11,
    np.array([1,1]):12,
    np.array([2,1]):13,
    np.array([3,1]):14,
    np.array([4,1]):15,
    np.array([5,1]):16,
    np.array([6,1]):17,
    np.array([7,1]):18,
    np.array([8,1]):19,
    np.array([9,1]):20,
    np.array([10,1]):21,
    np.array([11,1]):'dead',
    np.array([12,1]):119,

    np.array([0,2]):32,
    np.array([1,2]):31,
    np.array([2,2]):30,
    np.array([3,2]):29,
    np.array([4,2]):28,
    np.array([5,2]):27,
    np.array([6,2]):26,
    np.array([7,2]):25,
    np.array([8,2]):24,
    np.array([9,2]):23,
    np.array([10,2]):22,
    np.array([11,2]):'dead',
    np.array([12,2]):118,
    np.array([13,2]):120,

    np.array([0,3]):33,
    np.array([1,3]):34,
    np.array([2,3]):35,
    np.array([3,3]):36,
    np.array([4,3]):37,
    np.array([5,3]):38,
    np.array([6,3]):39,
    np.array([7,3]):40,
    np.array([8,3]):41,
    np.array([9,3]):42,
    np.array([10,3]):43,
    np.array([11,3]):'dead',
    np.array([12,3]):117,
    np.array([13,3]):121,
    np.array([14,3]):139,

    np.array([0,4]):54,
    np.array([1,4]):53,
    np.array([2,4]):52,
    np.array([3,4]):51,
    np.array([4,4]):50,
    np.array([5,4]):49,
    np.array([6,4]):48,
    np.array([7,4]):47,
    np.array([8,4]):46,
    np.array([9,4]):45,
    np.array([10,4]):44,
    np.array([11,4]):'dead',
    np.array([12,4]):116,
    np.array([13,4]):122,
    np.array([14,4]):138,
    np.array([15,4]):140,

    np.array([0,5]):55,
    np.array([1,5]):56,
    np.array([2,5]):57,
    np.array([3,5]):58,
    np.array([4,5]):59,
    np.array([5,5]):60,
    np.array([6,5]):61,
    np.array([7,5]):62,
    np.array([8,5]):63,
    np.array([9,5]):64,
    np.array([10,5]):65,
    np.array([11,5]):'dead',
    np.array([12,5]):115,
    np.array([13,5]):123,
    np.array([14,5]):137,
    np.array([15,5]):141,
    np.array([16,5]):159,

    np.array([0,6]):76,
    np.array([1,6]):75,
    np.array([2,6]):74,
    np.array([3,6]):73,
    np.array([4,6]):72,
    np.array([5,6]):71,
    np.array([6,6]):70,
    np.array([7,6]):69,
    np.array([8,6]):68,
    np.array([9,6]):67,
    np.array([10,6]):66,
    np.array([11,6]):'dead',
    np.array([12,6]):114,
    np.array([13,6]):124,
    np.array([14,6]):136,
    np.array([15,6]):142,
    np.array([16,6]):158,
    np.array([17,6]):160,

    np.array([0,7]):77,
    np.array([1,7]):78,
    np.array([2,7]):79,
    np.array([3,7]):80,
    np.array([4,7]):81,
    np.array([5,7]):82,
    np.array([6,7]):83,
    np.array([7,7]):84,
    np.array([8,7]):85,
    np.array([9,7]):86,
    np.array([10,7]):87,
    np.array([11,7]):'dead',
    np.array([12,7]):113,
    np.array([13,7]):125,
    np.array([14,7]):135,
    np.array([15,7]):143,
    np.array([16,7]):157,
    np.array([17,7]):161,
    np.array([18,7]):179,

    np.array([0,8]):98,
    np.array([1,8]):97,
    np.array([2,8]):96,
    np.array([3,8]):95,
    np.array([4,8]):94,
    np.array([5,8]):93,
    np.array([6,8]):92,
    np.array([7,8]):91,
    np.array([8,8]):90,
    np.array([9,8]):89,
    np.array([10,8]):88,
    np.array([11,8]):'dead',
    np.array([12,8]):112,
    np.array([13,8]):126,
    np.array([14,8]):134,
    np.array([15,8]):144,
    np.array([16,8]):156,
    np.array([17,8]):162,
    np.array([18,8]):178,
    np.array([19,8]):180,

    np.array([0,9]):99,
    np.array([1,9]):100,
    np.array([2,9]):101,
    np.array([3,9]):102,
    np.array([4,9]):103,
    np.array([5,9]):104,
    np.array([6,9]):105,
    np.array([7,9]):106,
    np.array([8,9]):107,
    np.array([9,9]):108,
    np.array([10,9]):109,
    np.array([11,9]):'dead',
    np.array([12,9]):111,
    np.array([13,9]):127,
    np.array([14,9]):133,
    np.array([15,9]):145,
    np.array([16,9]):155,
    np.array([17,9]):163,
    np.array([18,9]):177,
    np.array([19,9]):181,
    np.array([20,9]):199,

    np.array([0,10]):'dead',
    np.array([1,10]):'dead',
    np.array([2,10]):'dead',
    np.array([3,10]):'dead',
    np.array([4,10]):'dead',
    np.array([5,10]):'dead',
    np.array([6,10]):'dead',
    np.array([7,10]):'dead',
    np.array([8,10]):'dead',
    np.array([9,10]):'dead',
    np.array([10,10]):'dead',
    np.array([11,10]):'dead',
    np.array([12,10]):110,
    np.array([13,10]):128,
    np.array([14,10]):132,
    np.array([15,10]):146,
    np.array([16,10]):154,
    np.array([17,10]):164,
    np.array([18,10]):176,
    np.array([19,10]):182,
    np.array([20,10]):198,
    np.array([21,10]):200,

    np.array([1,11]):309,
    np.array([2,11]):310,
    np.array([3,11]):311,
    np.array([4,11]):312,
    np.array([5,11]):313,
    np.array([6,11]):314,
    np.array([7,11]):315,
    np.array([8,11]):316,
    np.array([9,11]):317,
    np.array([10,11]):318,
    np.array([11,11]):319,
    np.array([12,11]):'dead',
    np.array([13,11]):129,
    np.array([14,11]):131,
    np.array([15,11]):147,
    np.array([16,11]):153,
    np.array([17,11]):165,
    np.array([18,11]):175,
    np.array([19,11]):183,
    np.array([20,11]):197,
    np.array([21,11]):201,

    np.array([2,12]):308,
    np.array([3,12]):307,
    np.array([4,12]):306,
    np.array([5,12]):305,
    np.array([6,12]):304,
    np.array([7,12]):303,
    np.array([8,12]):302,
    np.array([9,12]):301,
    np.array([10,12]):300,
    np.array([11,12]):299,
    np.array([12,12]):298,
    np.array([13,12]):'dead',
    np.array([14,12]):130,
    np.array([15,12]):148,
    np.array([16,12]):152,
    np.array([17,12]):166,
    np.array([18,12]):174,
    np.array([19,12]):184,
    np.array([20,12]):196,
    np.array([21,12]):202,

    np.array([3,13]):287,
    np.array([4,13]):288,
    np.array([5,13]):289,
    np.array([6,13]):290,
    np.array([7,13]):291,
    np.array([8,13]):292,
    np.array([9,13]):293,
    np.array([10,13]):294,
    np.array([11,13]):295,
    np.array([12,13]):296,
    np.array([13,13]):297,
    np.array([14,13]):'dead',
    np.array([15,13]):149,
    np.array([16,13]):151,
    np.array([17,13]):167,
    np.array([18,13]):173,
    np.array([19,13]):185,
    np.array([20,13]):195,
    np.array([21,13]):203,

    np.array([4,14]):286,
    np.array([5,14]):285,
    np.array([6,14]):284,
    np.array([7,14]):283,
    np.array([8,14]):282,
    np.array([9,14]):281,
    np.array([10,14]):280,
    np.array([11,14]):279,
    np.array([12,14]):278,
    np.array([13,14]):277,
    np.array([14,14]):276,
    np.array([15,14]):'dead',
    np.array([16,14]):150,
    np.array([17,14]):168,
    np.array([18,14]):172,
    np.array([19,14]):186,
    np.array([20,14]):194,
    np.array([21,14]):204,

    np.array([5,15]):265,
    np.array([6,15]):266,
    np.array([7,15]):267,
    np.array([8,15]):268,
    np.array([9,15]):269,
    np.array([10,15]):270,
    np.array([11,15]):271,
    np.array([12,15]):272,
    np.array([13,15]):273,
    np.array([14,15]):274,
    np.array([15,15]):275,
    np.array([16,15]):'dead',
    np.array([17,15]):169,
    np.array([18,15]):171,
    np.array([19,15]):187,
    np.array([20,15]):193,
    np.array([21,15]):205,

    np.array([6,16]):264,
    np.array([7,16]):263,
    np.array([8,16]):262,
    np.array([9,16]):261,
    np.array([10,16]):260,
    np.array([11,16]):259,
    np.array([12,16]):258,
    np.array([13,16]):257,
    np.array([14,16]):256,
    np.array([15,16]):255,
    np.array([16,16]):254,
    np.array([17,16]):'dead',
    np.array([18,16]):170,
    np.array([19,16]):188,
    np.array([20,16]):192,
    np.array([21,16]):206,

    np.array([7,17]):243,
    np.array([8,17]):244,
    np.array([9,17]):245,
    np.array([10,17]):246,
    np.array([11,17]):247,
    np.array([12,17]):248,
    np.array([13,17]):249,
    np.array([14,17]):250,
    np.array([15,17]):251,
    np.array([16,17]):252,
    np.array([17,17]):253,
    np.array([18,17]):'dead',
    np.array([19,17]):189,
    np.array([20,17]):191,
    np.array([21,17]):207,

    np.array([8,18]):242,
    np.array([9,18]):241,
    np.array([10,18]):240,
    np.array([11,18]):239,
    np.array([12,18]):238,
    np.array([13,18]):237,
    np.array([14,18]):236,
    np.array([15,18]):235,
    np.array([16,18]):234,
    np.array([17,18]):233,
    np.array([18,18]):232,
    np.array([19,18]):'dead',
    np.array([20,18]):190,
    np.array([21,18]):208,

    np.array([9,19]):221,
    np.array([10,19]):222,
    np.array([11,19]):223,
    np.array([12,19]):224,
    np.array([13,19]):225,
    np.array([14,19]):226,
    np.array([15,19]):227,
    np.array([16,19]):228,
    np.array([17,19]):229,
    np.array([18,19]):230,
    np.array([19,19]):231,
    np.array([20,19]):'dead',
    np.array([21,19]):209,

    np.array([10,20]):220,
    np.array([11,20]):219,
    np.array([12,20]):218,
    np.array([13,20]):217,
    np.array([14,20]):216,
    np.array([15,20]):215,
    np.array([16,20]):214,
    np.array([17,20]):213,
    np.array([18,20]):212,
    np.array([19,20]):211,
    np.array([20,20]):210,
    np.array([21,20]):'dead',


}












