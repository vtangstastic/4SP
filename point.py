class Point:
  
  def read_points(self, file):
      with open(file, 'r') as f:
          no_points = int(f.readline())
          pointsx = []
          pointsy = []
          points = []

          for _ in range(no_points):
              line = f.readline().split()
              x = float(line[0])
              pointsx.append(x)
              y = float(line[1])
              pointsy.append(y)
              pt = (x,y)
              points.append(pt)

      return points, pointsx, pointsy
