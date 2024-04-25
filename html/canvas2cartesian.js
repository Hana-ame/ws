/**
 * 创建一个坐标转换器
 * @param centerX - canvas的中心x坐标
 * @param centerY - canvas的中心y坐标
 * @returns 一个包含两个函数的对象,分别用于坐标系之间的相互转换
 */
function createCoordinateConverter(centerX, centerY) {
    /**
     * 将canvas坐标系中的坐标转换为平面直角坐标系中的坐标
     * @param x - canvas坐标系中的x坐标
     * @param y - canvas坐标系中的y坐标
     * @returns 包含平面直角坐标系中x和y坐标的对象
     */
    function canvasToCartesian(x, y) {
        var cartesianX = x - centerX;
        var cartesianY = centerY - y;
        return { x: cartesianX, y: cartesianY };
    }
    /**
     * 将平面直角坐标系中的坐标转换为canvas坐标系中的坐标
     * @param x - 平面直角坐标系中的x坐标
     * @param y - 平面直角坐标系中的y坐标
     * @returns 包含canvas坐标系中x和y坐标的对象
     */
    function cartesianToCanvas(x, y) {
        var canvasX = x + centerX;
        var canvasY = centerY - y;
        return { x: canvasX, y: canvasY };
    }
    return { canvasToCartesian: canvasToCartesian, cartesianToCanvas: cartesianToCanvas };
}
