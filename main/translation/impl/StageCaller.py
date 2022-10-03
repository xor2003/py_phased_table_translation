#*
# * Calls actual translator to translate element.
# * <p>
# * Actual translator means closure specified for a particular stage.
# 
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @CompileStatic public class StageCaller<C> extends GroovyObjectSupport implements AroundElement<C>
class StageCaller(GroovyObjectSupport, AroundElement):
#JAVA TO PYTHON CONVERTER TODO TASK: Java annotations have no direct Python equivalent:
#ORIGINAL LINE: @Override public List<?> translateElement(@Nonnull String stageName, @Nonnull Closure<List<?>> stageCode, @Nullable Object element, @Nullable C context)
    def translateElement(self, stageName, stageCode, element, context):
#JAVA TO PYTHON CONVERTER TODO TASK: The following line could not be converted:
        return ((List<?>)(stageCode.call(element, context)));

    @staticmethod
    def _setGroovyRef(ref, newValue):
        ref.set(newValue)
        return newValue
