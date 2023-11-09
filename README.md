# connected_components
connected components analysis of an image that contains text in it is done and number of lines and words of the text is extracted from the image and also labeling is done.
<br /> As the text in the image is in black color, here I used erosion to separate words and lines.

## Erosion operation Description
This morphological operation consists of convolving an image A with some kernel ( B) and computes a local minimum over the area of given kernel.
As the kernel B is scanned over the image, we compute the minimal pixel value overlapped by B and replace the image pixel under the anchor point with that minimal value.
The erosion operation is: dst(x,y)=min(x′,y′):element(x′,y′)≠0src(x+x′,y+y′)

The result of this operation is in a way that the bright areas of the image get thinner, whereas the dark zones gets bigger.

## Results
__The Original Image is:__

![original image](https://github.com/ahmad-sohrabi/connected_components/blob/main/result/original.png?raw=true)

__The Labelled Lines Image is:__

![labelled lines image](https://github.com/ahmad-sohrabi/connected_components/blob/main/result/labelled_lines.png?raw=true)


__The Labelled words Image is:__

![labelled words image](https://github.com/ahmad-sohrabi/connected_components/blob/main/result/labelled_words.png?raw=true)
