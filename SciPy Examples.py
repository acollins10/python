import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,8]])

from scipy import linalg

linalg.det(A)
Out[4]: 2.999999999999997
# A=PLU P=permutation matrix, L=lower triangular with unit diagonal elements, and U=upper triangular.
P, L, U = linalg.lu(A)

P
Out[6]: 
array([[0., 1., 0.],
       [0., 0., 1.],
       [1., 0., 0.]])

L
Out[7]: 
array([[1.        , 0.        , 0.        ],
       [0.14285714, 1.        , 0.        ],
       [0.57142857, 0.5       , 1.        ]])

U
Out[8]: 
array([[7.        , 8.        , 8.        ],
       [0.        , 0.85714286, 1.85714286],
       [0.        , 0.        , 0.5       ]])

np.dot(L,U)
Out[9]: 
array([[7., 8., 8.],
       [1., 2., 3.],
       [4., 5., 6.]])
#  eigenvalues and eigenvectors of this matrix
EW, EV = linalg.eig(A)

EW
Out[11]: array([15.55528261+0.j, -1.41940876+0.j, -0.13587385+0.j])

EV
Out[12]: 
array([[-0.24043423, -0.67468642,  0.51853459],
       [-0.54694322, -0.23391616, -0.78895962],
       [-0.80190056,  0.70005819,  0.32964312]])
# Linear equations
v = np.array([[2],[3],[5]])

v
Out[14]: 
array([[2],
       [3],
       [5]])

s = linalg.solve(A,v)

s
Out[16]: 
array([[-2.33333333],
       [ 3.66666667],
       [-1.        ]])
# Sparse Linear Algebra
from scipy import sparse

 A = sparse.lil_matrix((1000, 1000))

A
Out[19]: 
<1000x1000 sparse matrix of type '<class 'numpy.float64'>'
	with 0 stored elements in LInked List format>

A[0,:100] = np.random.rand(100)

A[1,100:200] = A[0,:100]

A.setdiag(np.random.rand(1000))

A
Out[23]: 
<1000x1000 sparse matrix of type '<class 'numpy.float64'>'
	with 1199 stored elements in LInked List format>
# Using sparse linear algebra to construct very large matrix
from scipy.sparse import linalg

A.tocsr()
Out[25]: 
<1000x1000 sparse matrix of type '<class 'numpy.float64'>'
	with 1199 stored elements in Compressed Sparse Row format>

A = A.tocsr()

b = np.random.rand(1000)

linalg.spsolve(A, b)
Out[28]: 
array([ 1.02915228e+03, -7.85583876e+02,  7.61953672e-01,  3.45776825e-01,
        3.83563609e-01,  1.28994524e+01,  6.50914349e-01,  2.19035486e+00,
        1.13218127e+00,  1.51082314e-01,  4.62628171e-01,  5.83295740e-01,
        3.91205168e-02,  1.88571795e-01,  1.86687801e+00,  2.65111610e+00,
        1.68807545e-01,  5.73963129e-01,  3.52168601e-01,  1.52507698e+00,
        8.04053593e-01,  1.20538926e+00,  7.07025229e-01,  2.80672030e-01,
        1.57497657e+00,  6.56527222e-01,  1.00865551e+00,  3.54420461e-01,
        7.27046400e-01,  3.51571169e+00,  5.54786769e-01,  2.32975265e+00,
        7.38424849e-01,  7.83093560e+00,  2.38245530e+00,  3.24374834e-01,
        1.38672018e-01,  1.43731479e+00,  9.25715643e-01,  2.45526256e+00,
        1.14452790e+00,  1.59577685e+00,  7.17544015e-01,  2.43724628e+00,
        3.06250473e+00,  7.22986631e-01,  8.60082386e-01,  1.29276469e+00,
        1.94882135e-01,  3.05958909e-01,  1.09775666e+00,  1.40682936e+00,
        3.44682165e+00,  3.68727951e+00,  3.09483754e+00,  1.73739779e+00,
        3.53610331e-01,  3.54584049e-01,  6.88898026e-01,  5.22383288e-02,
        2.52743528e+00,  1.47667794e+00,  3.51180988e+00,  5.45707105e-01,
        1.72616468e+00,  3.97246423e-01,  2.70985254e-01,  1.10874974e+00,
        7.59075200e-01,  1.78449245e+00,  9.55101661e-01,  9.52580159e-01,
        3.70062246e-03,  1.11776120e+00,  3.62733486e+00,  2.28489015e+00,
        3.55785700e+00,  9.36891042e-01,  1.00812601e+00,  5.95855465e+00,
        1.87497977e+00,  2.77480244e-01,  2.47217183e+00,  5.37156087e-01,
        1.33981462e+00,  1.05382876e+00,  2.00980174e+00,  3.04594547e-01,
        1.36604879e+00,  5.00301680e-01,  1.05789970e+00,  1.10534835e+00,
        1.82800451e+00,  6.90723557e-01,  7.42358600e-01,  3.92534736e-01,
        8.47053797e-01,  8.10683131e-01,  5.91754527e-01,  2.20513754e+00,
        1.70194094e+00,  4.77379758e-01,  4.93438797e-01,  7.60028238e-01,
        1.05214351e+00,  1.17144585e+00,  2.02136733e+00,  1.15763631e+00,
        2.13115610e-01,  1.03152648e+00,  1.09874514e+00,  4.11573651e+01,
        5.20793207e-01,  8.14751096e-02,  6.65360809e-01,  1.42218496e+00,
        3.63036233e-01,  3.03956925e+00,  9.11374246e-01,  1.16839484e+00,
        8.86128025e+00,  1.59963991e+00,  8.92217793e-01,  1.59773377e+00,
        6.28637254e-02,  2.86405178e-02,  6.20571412e-02,  3.83303159e-01,
        1.33601561e-01,  7.16198616e-01,  5.26211923e+00,  2.36151583e+00,
        4.04387226e-01,  1.20220497e+00,  3.85682141e-01,  1.71365875e+00,
        1.14501962e+00,  8.02957907e-01,  6.85836827e-01,  1.85690656e+00,
        2.69205034e-01,  1.30553004e-01,  1.61835944e+00,  2.09610521e-01,
        2.96371085e+00,  6.51789334e-01,  1.88000637e-01,  4.74475610e+00,
        2.69741433e-01,  1.30705247e+00,  1.59899317e+00,  1.10503381e+00,
        5.20574388e-01,  2.48947383e+00,  8.56869934e-01,  1.06071819e+00,
        1.13047659e+00,  1.10838563e+00,  1.95269359e+00,  1.23266303e+01,
        2.46265137e+02,  1.50586512e+00,  1.42263894e+00,  2.05206006e+00,
        4.50340299e-01,  1.84012987e+00,  5.19285478e-01,  1.50123236e+00,
        1.21916049e+01,  5.08866550e-01,  4.32286994e-01,  3.90583724e+00,
        8.08808467e-01,  1.26682843e+00,  3.39009289e+00,  6.75563251e+00,
        5.13427692e-01,  3.62710923e+00,  2.98955852e-01,  2.42742355e+00,
        1.56560119e+00,  8.65825273e-01,  1.38655414e+00,  9.44816736e-01,
        1.03958937e+00,  7.60738096e-01,  1.60733704e+00,  3.07165878e-01,
        8.74813121e-01,  1.29135980e+00,  1.05572900e+00,  1.89617861e-01,
        8.99910153e-01,  1.21038203e+00,  7.46770060e-01,  5.87865951e-01,
        1.02486465e+01,  3.09131781e+00,  2.20544018e+01,  1.09263313e+00,
        6.79350442e-01,  9.88987374e+00,  3.30179670e+00,  9.43606296e-01,
        8.40064265e-02,  1.75966955e+00,  1.18119212e+00,  1.31282021e+00,
        1.00098111e+00,  6.32787099e+00,  1.82423135e+00,  4.58716076e-01,
        2.60411022e+01,  9.80704504e+00,  3.08694126e-02,  1.99029992e+01,
        2.54152079e+00,  2.19607660e+00,  2.30108054e-01,  5.16025343e-01,
        2.69117015e+00,  6.75256979e-01,  6.33801753e+01,  5.91745397e-02,
        2.16567924e+00,  9.93114216e-01,  2.48983829e+00,  1.56409373e-01,
        1.52018571e+00,  1.23074530e+00,  3.22748348e-01,  1.89083559e-02,
        1.75113768e+00,  2.63047754e-01,  6.82033576e-01,  6.74409110e+00,
        5.98211803e-01,  6.17525444e-01,  1.93902643e+00,  4.96996698e-01,
        2.05206598e+00,  1.62570172e+00,  2.64356914e+00,  5.76631407e-01,
        4.93258468e-01,  1.08418833e+00,  8.46826054e-01,  7.74318697e-01,
        2.40495852e+00,  1.07688929e-01,  2.25936716e+00,  1.02596004e+00,
        6.10836429e-01,  5.60726906e-01,  8.46469754e-01,  6.39596501e-01,
        1.13473718e+00,  2.22618351e+00,  1.32999984e+00,  2.23521197e+00,
        1.00287836e+00,  1.12015451e+00,  8.78140035e-01,  3.16988397e+00,
        4.41428802e+00,  9.65724507e-01,  5.22462559e-01,  5.11382898e+00,
        6.81101940e-01,  1.12996495e+00,  1.87036540e+00,  1.68260081e+00,
        1.01706118e+00,  6.21825854e-01,  5.66524608e-01,  7.09123671e+00,
        8.20335657e-01,  1.59495649e+00,  3.88488721e+00,  1.51251302e+00,
        1.15341655e-01,  1.96533878e+00,  6.89439110e-01,  2.66355711e+00,
        3.39032587e+00,  1.66023245e+00,  1.27123032e+00,  2.06481190e+00,
        8.74518876e-01,  3.21021314e-01,  1.28636610e+00,  3.96082450e-01,
        9.79896649e-01,  2.78999958e-01,  2.31156094e+00,  2.83281375e-01,
        1.87939827e+00,  4.55866138e-01,  8.37026945e-01,  6.86489247e-01,
        4.19390558e-01,  1.10165230e-01,  5.93161893e-01,  7.69405440e-01,
        1.38280299e+00,  3.76100820e+00,  8.86804221e-01,  2.21516214e+00,
        2.24420246e+00,  2.32842197e+00,  8.82727067e-01,  1.57762807e+00,
        1.21401402e+00,  6.88870649e-02,  2.18041343e-01,  1.68302866e+00,
        6.33168557e-01,  7.87879780e-01,  1.42245917e+00,  8.51416085e-01,
        1.29370075e+00,  2.42492718e+00,  1.20066860e+00,  7.65849030e-01,
        2.58527775e-01,  2.84911171e-01,  2.07102652e+00,  8.00444178e-01,
        3.47468402e-01,  1.01095441e+00,  8.46805468e-01,  3.18164729e-01,
        2.78383468e-01,  3.14784102e-01,  7.71722670e-01,  2.08644212e+01,
        1.19087179e-01,  6.18843695e-01,  7.69304633e+00,  1.21931251e-01,
        6.91085901e-01,  7.62369212e-01,  8.62254748e-01,  6.90111236e-01,
        5.45235480e-01,  1.53495868e-01,  3.19229240e+00,  4.86232519e-02,
        1.77469896e+00,  1.84105955e+00,  2.37351722e-01,  7.70915814e-01,
        1.33235874e+00,  7.98223166e-01,  7.56771204e-01,  1.20128920e+00,
        3.49043949e-01,  9.24872789e-01,  5.87618729e-01,  6.00389695e-01,
        1.10676071e-01,  1.77381093e+00,  1.23831841e+00,  1.59517997e+00,
        1.00363770e+00,  4.53547724e+00,  8.86198908e-01,  1.08424815e+01,
        6.85190863e+00,  3.68603887e-01,  8.77227560e+00,  1.14860618e+00,
        7.24090173e-01,  7.02799658e-01,  1.07584219e-01,  1.56531087e+01,
        3.73984460e-01,  1.12230526e+01,  1.47103511e+00,  2.98374235e+00,
        1.54605456e+00,  4.05530502e+00,  6.07138056e-01,  9.32110217e-01,
        1.03321778e+00,  2.32435593e+00,  1.13486384e+00,  2.36349394e+01,
        5.35019611e+00,  9.18760433e-01,  2.00326632e+00,  5.71866356e-01,
        4.71291038e-01,  6.30298524e-01,  2.68081327e+00,  1.50188192e-01,
        7.91552196e-01,  4.45922777e+00,  5.75101015e+00,  1.01841441e+00,
        3.15997136e-01,  2.03552459e-01,  1.64325617e+00,  9.25028506e-01,
        8.58452086e-01,  1.75504963e+00,  1.12994968e+00,  1.73845888e+01,
        3.74027907e+01,  2.87323875e+01,  2.36585847e+00,  5.67006313e-01,
        1.69684564e+00,  4.71875404e-01,  1.67980592e+00,  1.39017602e+00,
        4.08661959e+01,  3.60573015e-01,  3.48068835e-01,  1.73791641e+00,
        1.04764182e+00,  4.48486254e+00,  1.72901621e+00,  1.02249044e+00,
        1.29792296e+00,  1.10230324e+00,  4.77415027e+00,  3.17921367e-01,
        2.16406512e+00,  8.01499883e-01,  6.79660900e+00,  8.19200076e+00,
        2.50124143e+00,  2.20668577e+00,  2.59670737e-01,  4.20339961e-01,
        5.37680310e-01,  8.95858125e-01,  1.95640020e+00,  5.70557727e+00,
        5.11956073e-03,  1.65873064e+01,  8.41904347e-01,  3.18025533e+00,
        1.04070021e+00,  6.47503001e-01,  4.13290910e-01,  5.85508980e-01,
        2.04230731e+00,  8.67584117e-01,  2.44577426e+00,  1.48021663e+00,
        8.22226085e+00,  6.45889127e-01,  9.93879898e-02,  1.10142152e+00,
        7.11534004e-01,  1.00300159e+00,  4.64302204e-01,  2.01349219e+00,
        3.23320192e+00,  1.06355927e+00,  3.27795771e+00,  1.03597648e+00,
        5.33680777e-01,  7.45804755e-01,  7.19420806e+00,  8.57241757e-01,
        7.19000003e+00,  5.06993151e-01,  6.68723234e-01,  1.08361547e+00,
        5.78226493e-01,  7.65052001e-01,  7.60549562e-01,  9.93627258e-01,
        6.09567329e-01,  2.37749885e+01,  1.11375099e+00,  2.72101584e+00,
        2.68781921e+00,  4.93549810e-01,  1.27029851e+00,  1.19475979e+00,
        3.10455515e+00,  1.36943921e-01,  1.25210516e+00,  1.82832467e-01,
        6.55035533e-01,  2.14388094e+00,  1.85140788e-01,  1.44863054e-01,
        2.61305743e-01,  4.29945538e-01,  5.81531657e+00,  6.52318407e+00,
        6.25087995e-01,  7.15860167e-01,  3.23807827e-01,  2.02329857e+00,
        1.69301859e+01,  3.35082400e-01,  2.65493101e+00,  1.09152750e+00,
        4.05838451e-01,  1.28789995e+01,  1.06195118e-02,  9.10623571e-01,
        2.34067762e+00,  1.02009534e+00,  1.68146613e+00,  3.88987213e-01,
        6.12055339e-01,  5.78348155e-01,  1.90078889e-01,  3.27238276e-01,
        4.00385209e-01,  2.40607142e+00,  1.01701152e+00,  5.61799998e+00,
        1.12250079e+00,  1.11080003e+00,  6.58724060e-01,  5.04415887e-01,
        2.30530451e+00,  7.06749714e-01,  1.30320556e+00,  4.06696518e+00,
        5.69259067e+00,  1.08402787e-01,  2.71041004e+00,  1.87313413e+00,
        9.39009042e-01,  9.42521293e-01,  1.76071909e-01,  5.08826667e-01,
        7.36695163e-01,  1.05113911e+00,  1.38820374e+00,  2.96384975e+00,
        2.98109750e+00,  9.54919154e-01,  1.64390596e+00,  2.03191247e+00,
        9.90361989e-01,  1.90160508e+00,  2.76613566e-01,  4.89317845e-01,
        2.60656216e-01,  4.49999040e+00,  7.78250833e-02,  1.03268157e+00,
        1.38557802e+01,  9.32058643e-01,  1.38765282e+00,  5.85699949e-01,
        8.01776070e-01,  1.75407771e+00,  8.97507125e-02,  1.22261266e+00,
        6.85777410e-01,  3.86461164e+00,  2.10440559e+00,  6.23122920e-01,
        8.80242827e-01,  1.18626478e+00,  4.52883911e-01,  3.12905482e+00,
        8.09411171e-01,  1.20339395e+00,  6.61340434e-01,  1.61507842e+00,
        6.89400241e-01,  5.07632055e-01,  7.46279010e-01,  8.80171300e-01,
        2.13809657e+00,  1.05065107e+00,  5.99225481e-01,  9.31546459e-01,
        1.44631714e+00,  2.83392455e+01,  5.86242964e-01,  9.02919516e+00,
        4.83029020e-01,  9.13946630e-01,  4.21234385e+00,  9.38141579e-02,
        1.78085314e+00,  4.00439248e-01,  2.18046342e-01,  1.60232432e+00,
        7.74287494e-01,  6.45065872e-01,  6.48920062e-01,  4.01890584e-01,
        2.83584520e+00,  8.58522182e-01,  2.37741021e+00,  1.07845918e+00,
        8.03360583e+00,  4.98912850e-02,  2.89472127e-01,  2.68983151e-01,
        6.68010356e+00,  5.51130286e-01,  1.14012931e+01,  9.68122612e-02,
        1.37038050e+00,  8.58855693e-02,  4.43003230e-01,  1.57487360e+00,
        4.35125304e-01,  8.61453966e-02,  5.02415233e-01,  2.08954290e-01,
        1.11887648e+00,  3.10352716e+00,  1.84336232e+00,  8.95676902e-01,
        7.01200627e-02,  1.72356283e+00,  9.42450919e-01,  9.75137547e+00,
        2.58297641e+00,  1.15836960e+00,  5.12130160e-02,  7.76156966e-01,
        6.58978505e-01,  6.71795986e-01,  1.05671740e+00,  9.85318246e-01,
        9.48027769e-01,  2.75590716e+00,  2.07450387e+00,  6.01194081e+00,
        8.93810868e-01,  5.73395555e-01,  7.06237369e-01,  5.65224597e-01,
        1.01185269e+00,  2.20524001e+00,  1.51916723e+00,  5.89553929e-01,
        5.26677115e-01,  5.49907960e+00,  1.22072384e+00,  6.80033739e-03,
        7.29842049e-02,  5.82318964e+01,  3.66781499e-01,  3.79205785e+00,
        1.00742808e+00,  7.38874337e-02,  2.48098635e-02,  3.98318313e+00,
        2.06545120e+00,  5.81694159e-01,  9.48149769e-01,  6.17635298e-01,
        2.22845145e-01,  7.66438140e-01,  6.02503922e+00,  1.08381177e+00,
        6.61921269e-01,  8.08207787e-01,  1.17560729e+01,  1.06138493e-01,
        2.34944319e+00,  6.03745945e-01,  1.58581960e+00,  1.07871252e+00,
        7.47514484e-01,  6.69680305e-01,  4.47982725e+00,  1.18245953e+00,
        8.42601599e-01,  4.65761940e-01,  1.03266608e+00,  1.60453260e+00,
        1.34941886e-01,  9.22537531e-01,  6.55076722e+00,  1.12387674e+00,
        1.92856960e+01,  2.08866312e+00,  5.25607953e-01,  1.88243353e+00,
        1.57490180e+00,  1.86543692e+00,  9.99711923e-01,  7.08562487e-01,
        4.82836191e-01,  4.67297124e+00,  6.48211379e-01,  2.04896889e+00,
        7.35062737e-01,  5.34946287e+00,  1.69115452e+00,  4.56417262e-01,
        1.57603495e+00,  4.75460627e-01,  5.34495731e+00,  1.04642305e+00,
        2.33980073e-02,  9.31272197e-01,  9.21433726e-01,  3.54982276e-01,
        1.33020260e+00,  4.06096688e-01,  8.26196952e-02,  1.48341090e+00,
        1.38158082e+00,  3.88769564e-01,  4.15621615e+00,  1.13554538e+00,
        8.73697777e+00,  9.34159156e+00,  1.75785073e+00,  1.12380900e+00,
        1.57345799e+00,  9.17907828e-01,  4.62444258e-02,  1.26370373e-01,
        9.63936562e-04,  3.00851561e+00,  6.86636736e-01,  2.14884024e-01,
        6.00021371e+00,  5.13871342e-01,  1.04156409e+00,  1.32112232e+01,
        3.68312262e-01,  3.87397055e+00,  5.35361656e-01,  1.85708081e+00,
        6.99720648e-01,  2.51922834e+00,  8.57138153e-01,  7.89723999e-01,
        8.02307307e-01,  3.62126216e-01,  1.55624576e+00,  4.69884015e-01,
        1.45494045e-01,  1.26526709e+00,  1.20878279e-01,  2.25874979e+00,
        5.42560732e-01,  1.12963762e+00,  9.92019035e-01,  8.48333095e-01,
        1.08209212e+00,  1.46560734e+00,  1.69766292e+00,  4.82015304e-01,
        4.27020586e-01,  5.05881530e-01,  1.10157656e+00,  3.33137037e-02,
        1.40487681e+00,  5.71040016e-01,  3.45484320e-01,  6.24051923e-01,
        9.71717532e-02,  2.04479874e+00,  4.16438665e+00,  8.38164021e+00,
        5.97150068e-01,  2.08628390e+00,  1.01792497e+00,  4.36045047e-01,
        7.51092173e+00,  7.36471162e+00,  1.22812774e+00,  4.61599479e-01,
        1.32446346e+00,  1.17622858e-01,  1.57281343e+00,  4.12620191e+01,
        4.71643887e-01,  2.70348701e-02,  6.84264950e-01,  4.95554961e-01,
        7.88103667e-01,  1.77377064e+00,  7.58060251e-01,  5.19525085e-01,
        4.13771734e-01,  2.12476980e-01,  1.59672904e-01,  8.92738207e+00,
        5.42840570e-01,  1.01875938e+00,  2.75483925e+01,  2.70660552e+00,
        1.72297396e-01,  5.71698415e+00,  8.45410699e-01,  5.34881312e+00,
        3.47594215e+01,  3.74648974e+01,  3.93345406e-01,  1.72384924e+00,
        2.55443821e+00,  1.12123982e+00,  4.07703192e-01,  1.93856780e+00,
        1.90200740e+00,  1.38247549e-01,  1.13415573e+00,  2.03030808e-01,
        3.12525281e-01,  1.43732913e-01,  9.98920546e-01,  2.86648239e+00,
        2.44420366e-01,  1.18774101e-01,  7.30495417e-01,  2.72808402e+00,
        9.80386092e-01,  3.78131891e-01,  1.00821419e+00,  2.35402023e-01,
        1.67576639e+00,  2.33037876e-01,  4.12740203e-01,  1.01117079e+01,
        5.18507500e+00,  9.04978665e-01,  1.78564919e+00,  5.48789748e-01,
        2.65539723e-01,  1.45131357e+00,  9.31669116e-01,  1.49966948e+00,
        1.70298596e+00,  3.24600598e+00,  3.89158013e+00,  8.24580368e-01,
        1.84392048e-01,  1.39629092e+00,  2.19442967e+00,  1.00273607e-01,
        8.73454168e-02,  9.72882991e-01,  1.05990748e-01,  1.48721472e+00,
        7.17068961e-01,  2.49366272e+00,  5.38539603e-02,  5.73931268e-01,
        3.58023145e+00,  1.48799430e+01,  2.38399105e+00,  1.14826091e+00,
        1.21110696e+00,  3.35834178e-01,  1.35568225e+00,  1.17984125e+00,
        3.28911960e-01,  4.66148069e-01,  4.25840791e-01,  7.86083529e-02,
        8.08128611e-02,  3.17492645e+00,  7.97102474e+00,  1.43058091e+00,
        1.66010479e+00,  6.62584202e+00,  1.16598231e+00,  8.09000308e-01,
        9.26211430e-01,  1.01279100e+00,  1.94892372e+00,  1.93205879e+00,
        6.80219091e-01,  1.35603284e-01,  3.10760922e-01,  1.77973485e+00,
        3.89154768e+00,  7.33088855e-01,  1.03203332e+00,  6.00012039e+00,
        1.41041382e+00,  7.27725103e+01,  1.24907319e+00,  1.70461445e+00,
        1.19877205e+00,  8.80095524e-01,  1.65177074e+00,  1.69279936e+01,
        7.55329839e-01,  1.60417311e+00,  2.77562654e+00,  6.50485823e-01,
        1.14357330e+00,  6.57984937e-01,  3.39753643e-01,  9.12797923e-01,
        4.46661748e+00,  1.24900648e+00,  1.90089916e+00,  5.09668627e-01,
        2.98508591e+00,  2.40370344e-01,  2.26215357e+00,  1.39531166e-01,
        8.21717852e-01,  4.59508012e-01,  1.66132647e+00,  7.77821341e-01,
        2.14115414e-01,  1.47523448e+00,  2.62354413e-01,  1.16545508e+00,
        1.16133319e+00,  1.77284779e+00,  1.85341124e+00,  1.18953936e-01,
        2.82422075e-01,  1.24750632e-01,  9.57303955e+00,  9.71097031e-01,
        1.87486234e-01,  5.77500468e-01,  7.35407713e-01,  6.00986135e-01,
        1.20855362e+00,  3.34168903e-01,  6.58756552e-01,  6.55375399e-01,
        1.27048631e+00,  1.19738771e+00,  5.30314663e-02,  3.21786339e+00,
        9.65148694e-01,  9.91103707e-01,  5.34667972e+00,  1.13307147e+01,
        1.95462015e+00,  4.85698352e-01,  5.36272779e-02,  5.69744221e-01,
        9.08463116e+02,  8.19504172e-01,  8.91714593e-01,  8.72486788e-01,
        1.12751760e+00,  1.00793130e+00,  3.72110106e-01,  3.17609441e-01,
        9.90344733e-01,  4.84731131e-01,  1.63364814e-01,  3.79557212e+00,
        3.86359700e+00,  9.11744217e-01,  5.21449030e+01,  7.61317683e+00,
        7.69974342e-01,  3.48882587e-01,  9.44482069e-01,  1.39331656e+00,
        1.08591836e+01,  1.53361712e+00,  9.72617747e-01,  6.65450333e+00,
        9.71102000e-01,  1.12560174e+00,  1.03062055e-01,  8.63295684e-01,
        8.87343263e-01,  6.23048607e-01,  2.23931843e+00,  1.51391883e+00,
        3.35470066e-01,  3.28447174e-02,  1.35266845e-01,  6.47999880e-01,
        2.10696677e+00,  4.71975309e-01,  8.66423734e-01,  8.80848993e-01,
        1.66061457e+00,  1.55520808e+00,  2.67639277e+00,  2.94265222e-01,
        1.25819942e+00,  5.18636011e-01,  3.73313678e+00,  3.38878943e+00,
        8.20347340e-01,  3.66408763e-01,  2.33092580e+00,  1.67359061e-01,
        5.27938056e-01,  7.64636265e+01,  3.52931586e-01,  7.81812655e-01])
