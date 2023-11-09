import cv2 as cv
import numpy as np

if __name__ == '__main__':
    originalImage = cv.imread("text.jpg", 0)

    erosionKernel = np.ones((20, 150), np.uint8)
    erosionKernelForWords = np.ones((7, 14), np.uint8)

    lines = cv.erode(originalImage, erosionKernel, iterations=1)
    words = cv.erode(originalImage, erosionKernelForWords, iterations=1)

    total_labels, labels, stats, centroid = cv.connectedComponentsWithStats(~lines, 4, cv.CV_32S)
    total_labels_words, labels_words, stats_words, centroid_words = cv.connectedComponentsWithStats(~words, 4,
                                                                                                    cv.CV_32S)

    lineColors = np.random.randint(0, 255, size=(total_labels, 3), dtype=np.uint8)
    lineColors[0] = [0, 0, 0]
    colored_lines = lineColors[labels]

    lineColors_words = np.random.randint(0, 255, size=(total_labels_words, 3), dtype=np.uint8)
    lineColors_words[0] = [0, 0, 0]
    colored_words = lineColors_words[labels_words]

    print(f"Total Number of lines are: {total_labels - 1}")
    print(f"Total Number of words are: {total_labels_words - 1}")

    cv.imshow("original Image", originalImage)
    cv.imshow("Colored Lines", colored_lines)
    cv.imshow("Colored Words", colored_words)

    cv.waitKey(0)
    cv.destroyAllWindows()
