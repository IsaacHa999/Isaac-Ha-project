import java.util.Arrays;

public class DoubleArraySeq implements Cloneable
{
    private double[] data;
    private int manyItems;
    private int currentIndex;

    /**
     * Initialize an empty seq with an initial capacity of 10. Note that the
     * addItem method works efficiently (without needing more
     * memory) until this capacity is reached.
     * @param-none
     * @PostCondition
     * This seq is empty and has an initial capacity of 10.
     * @exception OutOfMemoryError
     * Indicates insufficient memory for:
     * new double[10].
     **/
    public DoubleArraySeq( )
    {
        final int INITIAL_CAPACITY = 10;  //크기
        manyItems = 0;  //일단 요소는 0개
        data = new double[INITIAL_CAPACITY];
        currentIndex = 0;
    }
    /**
     * Initialize an empty seq with a specified initial capacity. Note that the
     * addItem method works efficiently (without needing more
     * memory) until this capacity is reached.
     * @param initialCapacity
     * the initial capacity of this seq
     * @precondition
     * initialCapacity is non-negative.
     * @postcondition
     * This seq is empty and has the given initial capacity.
     * @exception IllegalArgumentException
     * Indicates that initialCapacity is negative.
     * @exception OutOfMemoryError
     * Indicates insufficient memory for: new int[initialCapacity].
     **/
    public DoubleArraySeq(int initialCapacity)   //초기 크기 전달한다.
    {
        if (initialCapacity < 0)
            throw new IllegalArgumentException
                    ("The initialCapacity is negative: " + initialCapacity);
        data = new double[initialCapacity];  //data 생성
        manyItems = 0; /// 지금 요소는 0개다.
        currentIndex = 0;
    }

    /**
     * addBefore와 addAfter에 대한 주석
     용량이 부족하면 용량을 추가한다.
     * @param element
    postcondition:
    1. currentIndex 바로 앞 인덱스에 element가 추가된다.
    2. 삽입 후 new element가 currentIndex가 된다.
    3. 만약 current element가 없으면 addBefore는 front에 삽입한다.
    4. 만약 빈 sequence이면 첫 줄에 element를 추가한다.
     * @exception throws: OutOfMemoryError
     **/
    public void addBefore(double element)  ///element가 요소로 들어온다.
    {

        if (manyItems == data.length)
        { // Ensure twice as much space as we need.
            ensureCapacity((manyItems + 1)*2);
        }

        double[] copydata = new double[data.length+1];

        System.arraycopy(data, 0, copydata, 0, currentIndex);
        System.arraycopy(data, currentIndex, copydata, currentIndex + 1, manyItems);

        copydata[currentIndex] = element;

        data = copydata;
        manyItems++;
    }


    public void addAfter(double element)  ///element가 요소로 들어온다.
    {
        if (manyItems == data.length)
        { // Ensure twice as much space as we need.
            ensureCapacity((manyItems + 1)*2);
        }

        double[] copydata = new double[data.length + 1];

        System.arraycopy(data, 0, copydata, 0, currentIndex);
        System.arraycopy(data, currentIndex, copydata, currentIndex + 1, manyItems);
        copydata[currentIndex] = element;

        data = copydata;
        currentIndex++;

        manyItems++;      /// 요소 개수 +1   data = {element} 상황 manyitems == 1
    }

    /**
     * addAll에 대한 주석
     * @param addend
     * a sequence whose contents will be placed at the end of this sequence
     *
     * precondition: 파라미터 is not null.
     * portcondition: addend는 squence의 끝에 배치된다.
     * @exception NullPointerException
     * @exception OutOfMemoryError
     * @note
     * An attempt to increase the capacity beyond Integer.MAX_VALUE will cause this sequence to fail with an arithmetic overflow.
     **/
    public void addAll(DoubleArraySeq addend)
    {
        ensureCapacity(manyItems + addend.manyItems);
        System.arraycopy(addend.data, 0, data, manyItems, addend.manyItems);
        manyItems += addend.manyItems;
    }

    /**
     * advance()
     * current element를 ++한다.
     * Precondition: isCurrent() returns true
     * Postcondition: current element가 끝 요소라면 current element는 존재하지 않는다. 그렇지 않으면 새로운 요소는 current element 다음요소이다.
     * @exception IllegalStateException
     */
    public void advance()
    {
        if (this.isCurrent()) currentIndex ++;
    }


    /**
     * Generate a copy of this seq.
     * @param - none
     * @return
     * The return value is a copy of this seq. Subsequent changes to the
     * copy will not affect the original, nor vice versa.
     * @exception OutOfMemoryError
     * Indicates insufficient memory for creating the clone.
     **/
    public DoubleArraySeq clone()
    { // Clone an IntArrayBag object.
        DoubleArraySeq answer;
        try
        {
            answer = (DoubleArraySeq) super.clone( );
        }
        catch (CloneNotSupportedException e)
        { // This exception should not occur. But if it does, it would probably
            // indicate a programming error that made super.clone unavailable.
            // The most common error would be forgetting the "Implements Cloneable"
            // clause at the start of this class.
            throw new RuntimeException
                    ("This class does not implement Cloneable");
        }
        answer.data = data.clone( );
        return answer;
    }

    /**
     *
     * @param s1
     * the first of two sequences
     * @param s2
     * the second of two eequences
     * @precondition
     * Neither s1 nor s2 is null.
     * @return
     * a new sequence that has the elements of s1 followed by the elements of s2 (with no current element)
     * @exception NullPointerException
     * Indicates that one of the arguments is null.
     * @exception OutOfMemoryError
     * An attempt to increase the capacity beyond Integer.MAX_VALUE will cause this sequence to fail with an arithmetic overflow.
     **/
    public static DoubleArraySeq concatenation(DoubleArraySeq s1, DoubleArraySeq s2)
    {

        DoubleArraySeq answer = new DoubleArraySeq(s1.getCapacity( ) + s2.getCapacity( ));
        System.arraycopy(s1.data, 0, answer.data, 0, s1.manyItems);
        System.arraycopy(s2.data, 0, answer.data, s1.manyItems, s2.manyItems);
        answer.manyItems = s1.manyItems + s2.manyItems;
        return answer;
    }

    /**
     * Accessor method to count the number of occurrences of a particular element
     * in this seq.
     * @param target
     * the element that needs to be counted
     * @return
     * the number of times that target occurs in this seq
     **/
    public int countOccurrences(int target)
    {
        int answer;
        int index;
        answer = 0;
        for (index = 0; index < manyItems; index++)
            if (target == data[index])
                answer++;
        return answer;
    }
    /**
     * @param minimumCapacity
     * @postcondition
     * This sequence’s capacity has been changed to at least minimumCapacity.
     * @exception OutOfMemoryError
     * Indicates insufficient memory for: new int[minimumCapacity].
     **/
    public void ensureCapacity(int minimumCapacity)
    {
        double[ ] biggerArray;
        if (data.length < minimumCapacity)
        {
            biggerArray = new double[minimumCapacity];
            System.arraycopy(data, 0, biggerArray, 0, manyItems);
            data = biggerArray;
        }
    }

    /**
     * Accessor method to get the current capacity of this sequence
     * The add method works efficiently (without needing
     * more memory) until this capacity is reached.
     * @param - none
     * @return
     * the current capacity of this seq
     **/
    public int getCapacity( )
    {
        return data.length;
    }
    /**
     * getCurrent
     * @param-none
     * @exception IllegalStateException
     */
    public double getCurrent()
    {
        if (this.isCurrent()) return currentIndex;
        else return -1.0;
    }
    /**
     * isCurrent
     */
    public boolean isCurrent()
    {
        if (currentIndex >= 0 && currentIndex <= manyItems) return true; // 등호 체크요망
        else return false;
    }

    public void removeCurrent()
    {
        if (currentIndex == manyItems) currentIndex = -1;
        else currentIndex++;
    }

    /**
     * Remove one copy of a specified element from this seq.
     * @param target
     * the element to remove from the seq
     * @postcondition
     * If target was found in the seq, then one copy of
     * target has been removed and the method returns true.
     * Otherwise the seq remains unchanged and the method returns false.
     **/
    public boolean remove(int target)
    {
        int index; // The location of target in the data array.
        // First, set index to the location of target in the data array,
        // which could be as small as 0 or as large as manyItems-1; If target
        // is not in the array, then index will be set equal to manyItems;
        for (index = 0; (index < manyItems) && (target != data[index]); index++)
            // No work is needed in the body of this for-loop.
            ;
        if (index == manyItems)
            // The target was not found, so nothing is removed.
            return false;
        else
        { // The target was found at data[index].
            // So reduce manyItems by 1 and copy the last element onto data[index].
            manyItems--;
            data[index] = data[manyItems];
            return true;
        }
    }

    /**
     * Determine the number of elements in this seq.
     * @param - none
     * @return
     * the number of elements in this seq
     **/
    public int size( )
    {
        return manyItems;
    }

    public void start()
    {
        if (this.isCurrent() ) currentIndex = 0;
    }
    /**
     * Reduce the current capacity of this seq to its actual size (i.e., the
     * number of elements it contains).
     * @param - none
     * @postcondition
     * This seq's capacity has been changed to its current size.
     * @exception OutOfMemoryError
     * Indicates insufficient memory for altering the capacity.
     **/
    public void trimToSize( )
    {
        double[ ] trimmedArray;
        if (data.length != manyItems)
        {
            trimmedArray = new double[manyItems];
            System.arraycopy(data, 0, trimmedArray, 0, manyItems);
            data = trimmedArray;
        }
    }

    //DoubleArraySeq 데모 코드
    public static void main(String[] args) {
        System.out.println("//0 DoubleArraySeq 데모 프로그램");
        //생성자 확인
        DoubleArraySeq ds = new DoubleArraySeq();
        DoubleArraySeq ds1 = new DoubleArraySeq(20);
        System.out.println("//1 생성자 확인");
        System.out.println("ds data: " + Arrays.toString(ds.data));
        System.out.println("ds1 data 인수 20: " + Arrays.toString(ds1.data));

        //addAfter, addBefore 확인
        ds.addAfter(10.0);
        ds.addBefore(100.0);
        System.out.println("//2 addAfter, addBefore 확인");
        System.out.println("ds data: " + Arrays.toString(ds.data));
        System.out.println("ds getCurrent: " + ds.getCurrent());

        ds.addAfter(20.0);
        ds.addAfter(30.0);
        ds.addAfter(40.0);
        ds.addAfter(50.0);
        ds1.addAll(ds);

        System.out.println("//4 addAll 확인");
        System.out.println("ds data: " + Arrays.toString(ds.data));
        System.out.println("ds1 data: " + Arrays.toString(ds1.data));
        ds1.addAll(ds);
        System.out.println("addAll 이후 ds1 data: " + Arrays.toString(ds1.data));

        System.out.println("//5 Advance()");
        System.out.println("ds cetCurrent: " + ds.getCurrent());
        ds.advance();
        System.out.println("ds data: " + Arrays.toString(ds.data));
        System.out.println("Advance --> ds cetCurrent: " + ds.getCurrent());

        System.out.println("//6 concatenation");
        DoubleArraySeq ds3 = new DoubleArraySeq();
        ds3 = concatenation(ds,ds1);
        System.out.println("ds3 data = ds + ds1: " + Arrays.toString(ds3.data));

        System.out.println("//7 ensureCapacity: 생성자에서 확인 완료");
        System.out.println("//8 ds getCapacity");;
        System.out.println("ds getCapacity: "+ ds.getCapacity());

        System.out.println("//9 getCurrent()");
        System.out.println("ds cetCurrent: " + ds.getCurrent());

        System.out.println("//10 isCurrent");
        System.out.println("isCurrent: " + ds.isCurrent());

        System.out.println("//11 size()");
        System.out.println("ds size: " + ds.size());

        System.out.println("//12 start()");
        ds.start();
        System.out.println("ds start --> currnet: "+ ds.getCurrent() );

        System.out.println("//13 trimsize()");
        ds.trimToSize();
        System.out.println("ds trimsize: " + Arrays.toString(ds.data));

        System.out.println();
















    }
} 