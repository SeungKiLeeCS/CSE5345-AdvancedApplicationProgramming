import turtle
import csv
import sys

# 인풋을 받아서 대응하는 함수를 불러옵니다.
def draw_shape(shape):
    
    if shape == 1:
        draw_triangle()
    elif shape == 2:
        draw_square()
    elif shape == 3:
        draw_circle()
    else:
        print("주어진 선택지 내에서 선택해 주세요.")

# 대충 이런 식으로 되어있겠죠? 본인의 함수를 넣어도 좋습니다.
def draw_triangle():
    driver = turtle.Turtle()
    driver.forward(100)
    
    for i in range(2):
        driver.left(120)
        driver.forward(100)

    window = turtle.Screen()
    window.bgcolor("white")
    window.exitonclick()

        
def draw_square():
    driver = turtle.Turtle()

    for i in range(4):
        driver.forward(100)
        driver.right(90)
        
    window = turtle.Screen()
    window.bgcolor("white")
    window.exitonclick()

def draw_circle():
    driver = turtle.Turtle()
    turtle.circle(100)

    window = turtle.Screen()
    window.bgcolor("white")
    window.exitonclick()

# Main 입니다.
def main():
    # 여기서 인풋을 받아들이고, 그것을 draw_shape() 함수에 보냅니다.
    print("어떤 도형을 그릴까요? 번호를 선택해 주세요\n1. 삼각형\n2. 사각형\n3. 원\n")
    shape = int(input())
    draw_shape(shape)
    
if __name__ == "__main__":
    main()
