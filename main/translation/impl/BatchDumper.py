#*
# * Dumps to string batch of translated elements.
# * <p>
# * E - type of elements.
# * C - translation context.
# *
# * @see BatchDumper#dumpBatch
# 
class BatchDumper(GroovyObjectSupport):
    #    *
    #     * Dumps specified batch of elements to string.
    #     *
    #     :param batch:   Batch to be dumped or null if not specified.
    #     :param context: Translation context or null if not specified.
    #     * @return String representation of batch and/or context.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull public abstract String dumpBatch(@Nullable List<E> batch, @Nullable C context);
    def dumpBatch(self, batch, context):
        pass

    @staticmethod
    def setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue
