import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TriangleTest {

    @Test
    public void testInvalidTriangle() {
        assertEquals(TriangleType.INVALID, Triangle.classify(0, 0, 0));
        assertEquals(TriangleType.INVALID, Triangle.classify(-1, 2, 3));
        assertEquals(TriangleType.INVALID, Triangle.classify(1, -2, 3));
        assertEquals(TriangleType.INVALID, Triangle.classify(1, 2, -3));
    }

    @Test
    public void testEquilateralTriangle() {
        assertEquals(TriangleType.EQUILATERAL, Triangle.classify(5, 5, 5));
    }

    @Test
    public void testIsoscelesTriangle() {
        assertEquals(TriangleType.ISOSCELES, Triangle.classify(5, 5, 3));
        assertEquals(TriangleType.ISOSCELES, Triangle.classify(3, 5, 5));
        assertEquals(TriangleType.ISOSCELES, Triangle.classify(5, 3, 5));
    }

    @Test
    public void testScaleneTriangle() {
        assertEquals(TriangleType.SCALENE, Triangle.classify(3, 4, 5));
    }
}