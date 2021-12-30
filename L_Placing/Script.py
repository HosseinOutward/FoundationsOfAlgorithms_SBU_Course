import pygame
import random
import time


class Graphics:
    pixelCubeSize, page = 0, 0

    def __init__(self, grid, cubeSize):
        N=len(grid)
        self.cubeSize=cubeSize
        self.pixelCubeSize = N*cubeSize + N-1
        self.page = pygame.display.set_mode((self.pixelCubeSize, self.pixelCubeSize))
        self.redrawPage(grid)

    def redrawPage(self, grid):
        self.page.fill((0,0,0))
        N=len(grid)
        for i in range(N):
            for j in range(N):
                self.colorCube(i,j, self.randColor(grid[i][j]))

        pygame.display.update()

    def colorCube(self, i, j, color):
        pygame.draw.rect(self.page, color, (self.pixelPos(i), self.pixelPos(j), self.cubeSize, self.cubeSize))

    def pixelPos(self, i):
        return i * self.cubeSize + i

    def randColor(self, n):
        random.seed(n*6)
        ret = 0
        r = int(random.random() * 225)+30
        g = int(random.random() * 225)+30
        b = int(random.random() * 225)+30
        step = 256 / (n+1)
        for i in range(n):
            r += step
            g += step
            b += step
            r = int(r) % 256
            g = int(g) % 256
            b = int(b) % 256
            ret = (r, g, b)
        return ret

    def wait(self):
        while True:
            pygame.time.wait(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

def f(a, N, null_point, sp=[0,0], l_num=1):
    # if N==2, color all tile but leave the null tile
    if N==2:
        a[sp[0]][sp[1]]=l_num
        a[sp[0]+1][sp[1]]=l_num
        a[sp[0]][sp[1]+1]=l_num
        a[sp[0]+1][sp[1]+1]=l_num
        a[null_point[0]][null_point[1]]=0
    # recursive part
    else:
        N2=int(N/2)


            # find where null point is (0=NW, 1=NE, 2=SW, 3=SE)
        if null_point[0]<sp[0]+N2:
            if null_point[1]<sp[1]+N2: t=0
            else: t=2
        else:
            if null_point[1]<sp[1]+N2: t=1
            else: t=3

        # run recursive
            # a function to generate inputs for recursive call of f
        def f_alt(argv):
            return f(argv[0], argv[1], argv[2], argv[3], argv[4])
        def f_one(r):
            startPoint=[[sp[0], sp[1]],
                        [sp[0]+N2, sp[1]],
                        [sp[0], sp[1]+N2],
                        [sp[0]+N2, sp[1]+N2]]
            cube = [[sp[0]+N2-1, sp[1]+N2-1],
                    [sp[0]+N2, sp[1]+N2-1],
                    [sp[0]+N2-1, sp[1]+N2],
                    [sp[0]+N2, sp[1]+N2]]
            cube[t] = null_point
            return [a, N2, cube[r], startPoint[r], l_num]

            # color squers that dont include null point
        for i in [0,1,2,3]:
            if i!=t:
                l_num=f_alt(f_one(i))
            # color center tile to fix empty parts
        l_num=f(a, 2, null_point, [sp[0]+N2-1, sp[1]+N2-1], l_num)
            # last calling of f to fill the remaining squer
        l_num=f_alt(f_one(t))

    #Graphics(a, 20)
    return l_num+1

if __name__ == '__main__':
    N=2**int(input("K (N will be in form of 2^k) "))
    null_point=list(map(int, input("point where its empty (ex. 1 1) ").split()))
    start_time = time.time()
    a=[[0 for j in range(N)] for i in range(N)]
    f(a,N,null_point)
    print("done, with time: " + str((time.time() - start_time)*100000//1/1000) + "% (percent) of a seconds")
    gui=Graphics(a,20).wait()