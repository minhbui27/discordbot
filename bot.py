import discord
from discord.ext import commands
import sympy as sp
import numpy as np
import asyncio
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@client.command()
async def subtract(ctx, a: int, b: int):
    await ctx.send(a - b)

@client.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a * b)

@client.command()
async def divide(ctx, a: int, b: int):
    await ctx.send(a / b)

@client.command()
async def clear(ctx, num: int):
    await ctx.channel.purge(limit = num)
    


@client.command(aliases = ['add1d'])
async def add_vectors1d(ctx, *numbers):
    a = []
    a.append(numbers)
    print(a[0][0])
    print(a[0][1])
    list_a = []
    list_b = []
    for i in range(1,len(a[0][0])-1):
        if a[0][0][i] != ',':
            list_a.append(a[0][0][i])
    for j in range(1,len(a[0][1])-1):
        if a[0][1][j] != ',':
            list_b.append(a[0][1][j])
    arr_a = np.array(list_a)
    arr_b = np.array(list_b)
    print(arr_a)
    print(arr_b)
    await ctx.send(np.add(arr_a,arr_b))
"""
@client.command(aliases = ['add2d'])
async def add_vectors2d(ctx, rowA: int, colA: int, rowB: int, colB: int, *numbers):
    print(f"{rowA} {colA} {rowB} {colB} {numbers}")
    matrixA = np.empty([rowA,colA],dtype=np.float32)
    matrixB = np.empty([rowB,colB],dtype=np.float32)
    a = []
    a.append(numbers)
    list_a = []
    list_b = []
    for i in range(1,len(a[0][0])-1):
        if a[0][0][i] != ',' and a[0][0][i] != '-':
            list_a.append(a[0][0][i])
        elif a[0][0][i] == '-':
            list_a.append(-a[0][1][i+1])
            i += 1
    for j in range(1,len(a[0][1])-1):
        if a[0][1][j] != ',' and a[0][1][j] != '-':
            list_b.append(a[0][1][j])
        elif a[0][1][j] == '-':
            list_b.append(-a[0][1][j+1])
            j += 1
    tempA = 0
    tempB = 0
    print(list_a)
    print(list_b)
    for n in range(rowA):
        for m in range(colA):
            matrixA[n][m] = list_a[tempA]
            tempA += 1
    for n in range(rowB):
        for m in range(colB):
            matrixB[n][m] = list_b[tempB]
            tempB += 1
    print(matrixA)
    print(matrixB)
    await ctx.send(np.add(matrixA,matrixB))
"""
@client.command(aliases = ['subtractvectors'])
async def subtract_vectors(ctx, *numbers):
    a = []
    a.append(numbers)
    print(a[0][0])
    print(a[0][1])
    list_a = []
    list_b = []
    for i in range(1,len(a[0][0])-1):
        if a[0][0][i] != ',':
            list_a.append(a[0][0][i])
    for j in range(1,len(a[0][1])-1):
        if a[0][1][j] != ',':
            list_b.append(a[0][1][j])
    arr_a = np.array(list_a)
    arr_b = np.array(list_b)
    print(arr_a)
    print(arr_b)
    await ctx.send(np.subtract(arr_a,arr_b))

@client.command(aliases = ['dot1d'])
async def multiply_matrices1d(ctx, *numbers):
    a = []
    a.append(numbers)
    print(a[0][0])
    print(a[0][1])
    list_a = []
    list_b = []
    for i in range(1,len(a[0][0])-1):
        if a[0][0][i] != ',':
            list_a.append(a[0][0][i])
    for j in range(1,len(a[0][1])-1):
        if a[0][1][j] != ',':
            list_b.append(a[0][1][j])
    arr_a = np.array(list_a)
    arr_b = np.array(list_b)
    print(arr_a)
    print(arr_b)
    await ctx.send(np.dot(arr_a,arr_b))

@client.command(aliases = ['dot2d'])
async def multiply_matrices2d(ctx, rowA: int, colA: int, rowB: int, colB: int, matA: str, matB):
    print(f"{rowA} {colA} {rowB} {colB} {matA} {matB}")
    matrixA = np.empty([rowA,colA],dtype=np.float32)
    matrixB = np.empty([rowB,colB],dtype=np.float32)
    matA = matA.strip("[]")
    matB = matB.strip("[]")
    a = np.fromstring(matA, dtype = np.float32, sep = ',')
    b = np.fromstring(matB, dtype = np.float32, sep = ',')
    tempA = 0
    tempB = 0
    for n in range(rowA):
        for m in range(colA):
            matrixA[n][m] = a[tempA]
            tempA += 1
    for n in range(rowB):
        for m in range(colB):
            matrixB[n][m] = b[tempB]
            tempB += 1
    print(matrixA)
    print(matrixB)
    await ctx.send(np.dot(matrixA,matrixB))


@client.command(aliases = ['inverse'])
async def inverse_matrix(ctx, rowA: int, colA: int , numbers: str):
    print(f"{rowA} {colA} {numbers}")
    matrixA = np.empty([rowA,colA],dtype=np.float32)
    numbers = numbers.strip("[]")
    a = np.fromstring(numbers, dtype = np.float32, sep = ',')
    tempA = 0
    for n in range(rowA):
        for m in range(colA):
            matrixA[n][m] = a[tempA]
            tempA += 1
    print(matrixA)
    
    await ctx.send(np.linalg.inv(matrixA))

@client.command(aliases = ['transpose'])
async def transpose_matrix(ctx, rowA: int, colA: int , numbers: str):
    print(f"{rowA} {colA} {numbers}")
    matrixA = np.empty([rowA,colA],dtype=np.float32)
    numbers = numbers.strip("[]")
    a = np.fromstring(numbers, dtype = np.float32, sep = ',')
    tempA = 0
    for n in range(rowA):
        for m in range(colA):
            matrixA[n][m] = a[tempA]
            tempA += 1
    print(matrixA)
    
    await ctx.send(np.transpose(matrixA))

@client.command(aliases = ['row_reduce'])
async def rref(ctx, rowA: int, colA: int , numbers: str):
    matrixA = np.empty([rowA,colA],dtype=np.int32)
    numbers = numbers.strip("[]")
    a = np.fromstring(numbers, sep = ',',dtype=np.int32)
    tempA = 0
    print(a)
    for n in range(rowA):
        for m in range(colA):
            matrixA[n][m] = a[tempA]
            tempA += 1
    print(matrixA)
    tempMatrix = sp.Matrix(matrixA).rref()
    resultMatrix = np.array(tempMatrix[0])
    pivotColumns = list(tempMatrix[1])
    for j in range(len(pivotColumns)):
        pivotColumns[j] += 1
    await ctx.send(f"{resultMatrix} \npivot columns: {pivotColumns}")

@client.command(aliases=['rand'])
async def random_matrix(ctx, rowA: int, colA: int):
    print(f"{rowA} {colA}")
    await ctx.send(np.random.rand(rowA,colA))

client.run('NzYyMTE0MzcxMjExMTAwMTYx.X3kcUQ.Cmq0UWljb6fujZE1vsQpqD5R-90')