
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees Can you do this in place?

# Here is an example for a 100, 100

# 0, 0 -> 100, 0
# 100, 0 -> 100, 100
# 100, 100 -> 0, 100
# 0, 100 -> 0, 0
#
# 1, 0 -> 100, 1
# 100, 1 -> 100, 99
# 100, 99 -> 0, 99
# 0, 99 -> 1, 0
#
# 2, 0 -> 100, 2
# 100, 2 -> 100, 98
# 100, 98 -> 0, 98
# 0, 98 - 2, 0

# Is a recursive case ok?
#   Yes, but I want an iterative one

# Can I use numpy matrices to represent this?
#   No

def rotate_img(img):
    n = len(img)
    half = n // 2
    i = 0

    while(i < half):

        j = i

        while(j < n - i - 1):
            top_left = img[i][j]

            top_right = img[n-j-1][i]
            img[n-j-1][i] = top_left

            bottom_right = img[n-i-1][n-j-1]
            img[n-i-1][n-j-1] = top_right

            bottom_left = img[j][n-i-1]
            img[j][n-i-1] = bottom_right

            img[i][j] = bottom_left

            j += 1

        i += 1

    return img

if __name__ == "__main__":
    img = [[1,2,3],[4,5,6],[7,8,9]]
    print(img)
    print(rotate_img(img))
    img2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(img2)
    print(rotate_img(img2))




