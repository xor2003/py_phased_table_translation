#*
# * Translates a batch of elements.
# * <p>
# * O - type of source elements.
# * R - type of result elements.
# * C - type of translation context.
# 
class BatchTranslator(GroovyObjectSupport):
    #    *
    #     * Translates a batch of elements.
    #     *
    #     * @param elements Elements to translate or empty list or null if none.
    #     * @param context  Translation context or null if none.
    #     * @return Translated elements or empty list if input was null.
    #     
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Nonnull public abstract List<R> translateBatch(@Nullable List<O> elements, @Nullable C context);
    def translateBatch(self, elements, context):
        pass
