#*
# * Dumps element per line using {@link Object#toString()}.
# * <p>
# * When dumping batches, each element will be placed on a new line.
# * Start of each element will be indicated with bullet and all elements
# * of batch will be numbered for easier identification.
# * This can be controlled via {@link FormattingToStringDumper#dumpBatchToBuffer}.
# * <p>
# * When dumping stages, an arrow near stage name will indicate if stage receives our outputs following
# * data.
# * <p>
# * Individual elements will be converted to strings using their toString
# * method. This can be controlled via
# * {@link FormattingToStringDumper#dumpElementToBuffer}.
# * <p>
# * {@link StringBuilder} is used internally to concatenate all necessary information.
# * {@link FormattingToStringDumper#estimatedDumpedEventSize} can be adjusted
# * to avoid resizing of this buffer.
# * <p>
# * E - type of elements.
# * C - translation context.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class FormattingToStringDumper<E, C> extends GroovyObjectSupport implements BatchDumper<E, C>, StageDumper<C>
class FormattingToStringDumper(GroovyObjectSupport, BatchDumper, StageDumper):

    def __init__(self):
        #instance fields found by Java to Python Converter:
        self._dumpBatchToBuffer = None


    class ClosureAnonymousInnerClass2(Closure):
        def __init__(self):
            super().__init__(outerInstance, outerInstance)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: public Object doCall(final String stageName)
        def doCall(self, stageName):
            return String.invokeMethod("valueOf", [getMetricsBaseName()]) + String.invokeMethod("valueOf", [stageName]) + ".one".invokeMethod("toString", [])


    class MetricSupplierAnonymousInnerClass(MetricRegistry.MetricSupplier):
        def newMetric(self):
            return Timer()

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public String dumpBatch(@Nullable List<E> batch, @Nullable C context)
    def dumpBatch(self, batch, context):
        buffer = self.makeBufferForBatch(batch)
        self.getDumpBatchToBuffer()
        return (str((buffer.invokeMethod("toString", []))))

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public String dumpBeforeStage(@Nonnull String stageName, @Nullable List<?> batch, @Nullable C context)
    def dumpBeforeStage(self, stageName, batch, context):
        buffer = self.makeBufferForBatch(batch)
        buffer << stageName << " <- "
        self.getDumpBatchToBuffer()
        return (str((buffer.invokeMethod("toString", []))))

#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public String dumpAfterStage(@Nonnull String stageName, @Nullable List<?> batch, @Nullable C context)
    def dumpAfterStage(self, stageName, batch, context):
        buffer = self.makeBufferForBatch(batch)
        buffer << stageName << " -> "
        self.getDumpBatchToBuffer()
        return (str((buffer.invokeMethod("toString", []))))

    #    *
    #     * Creates a buffer to hold batch dump.
    #     * <p>
    #     * By default, will allocate new buffer using batch size
    #     * and {@link #estimatedDumpedEventSize} to try to avoid resizing.
    #     *
    #     :param batch: Batch to be dumped or null if none.
    #     * @return Buffer where batch should be dumped.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: protected StringBuilder makeBufferForBatch(@Nullable List<?> batch)
    def makeBufferForBatch(self, batch):
        bufferSize = (batch.invokeMethod("size", []) + 1) * estimatedDumpedEventSize if batch.invokeMethod("size", []) else estimatedDumpedEventSize
        return StringBuilder(bufferSize)

    def getDumpBatchToBuffer(self):
        return self._dumpBatchToBuffer

    def setDumpBatchToBuffer(self, dumpBatchToBuffer):
        self._dumpBatchToBuffer = dumpBatchToBuffer

    def getDumpElementToBuffer(self):
        return dumpElementToBuffer

    def setDumpElementToBuffer(self, dumpElementToBuffer):
        self.dumpElementToBuffer = dumpElementToBuffer

    def getEstimatedDumpedEventSize(self):
        return estimatedDumpedEventSize

    def setEstimatedDumpedEventSize(self, estimatedDumpedEventSize):
        self.estimatedDumpedEventSize = estimatedDumpedEventSize

    #    *
    #     * Dumps a batch of elements.
    #     * <p>
    #     * The closure should take three parameters:
    #     * <ol>
    #     *     <li>List<?> events - a batch of elements to be dumped (could be null)</li>
    #     *     <li>Object context - Translation context (could be null).
    #     *     <li>StringBuilder buffer - buffer where to dump elements to</li>
    #     * </ol>
    #     * <p>
    #     * By default, each element will be placed on a new line.
    #     * <p>
    #     * Individual elements are dumped using {@link #dumpElementToBuffer}.
    #     

    #    *
    #     * Dumps individual element.
    #     * <p>
    #     * The closure should take two parameters:
    #     * <ol>
    #     *     <li>Object element - element to be dumped (could be null)</li>
    #     *     <li>Object context - Translation context (could be null).
    #     *     <li>StringBuilder buffer - buffer into which to dump event</li>
    #     * </ol>
    #     * <p>
    #     * By default, uses {@link StringBuilder#append(java.lang.Object)} which
    #     * will call {@link Object#toString()} in most cases.
    #     
    #    *
    #     * Estimated size of text of event dump.
    #     * <p>
    #     * This is used to create buffer of enough capacity to avoid re-sizing
    #     * during event tracing.
    #     * <p>
    #     * Default is 10K.
    #     

    @staticmethod
    def setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue

    class ClosureAnonymousInnerClass(Closure):
        def __init__(self):
            super().__init__(outerInstance, outerInstance)

#JAVA TO PYTHON CONVERTER TODO TASK: There is no Python equivalent to Java's 'final' parameters:
#ORIGINAL LINE: public Object doCall(List<?> elements, final Object context, final StringBuilder buffer)
        def doCall(self, elements, context, buffer):
            if elements is None.asBoolean():
                buffer << "null batch with context " << context
                return


            buffer << "["
            elements.invokeMethod("eachWithIndex", [ClosureAnonymousInnerClass3(self, DUMMY__1234567890_DUMMYYYYYY___.this, DUMMY__1234567890_DUMMYYYYYY___.this, buffer)])
            if not elements.empty.asBoolean():
                buffer << "|- end of batch"

            return buffer << System.invokeMethod("lineSeparator", []) << "] with context " << context

        class ClosureAnonymousInnerClass3(Closure):


            def __init__(self, outerInstance, self, self, buffer):
                super().__init__(self, self)
                self._outerInstance = outerInstance
                self._buffer = buffer

            def doCall(self, element, index):
                self._buffer << System.invokeMethod("lineSeparator", []) << "|- " << index << " "
                return outerInstance.outerInstance.getDumpElementToBuffer()


        class ClosureAnonymousInnerClass2(Closure):
            def __init__(self):
                super().__init__(outerInstance, outerInstance)

            def doCall(self, element, context, buffer):
                return buffer << element

