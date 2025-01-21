
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MetrologicalSymbolModule import MetrologicalSymbol



from .MathematicalSymbolModule import MathematicalSymbol



from .ConstantModule import Constant



from .MetrologicalModule import Metrological



from .SymbolModule import Symbol







class MetricPrefix(MetrologicalSymbol, MathematicalSymbol, Constant, Metrological, Symbol):
    """
    Class representing the `MetricPrefix` entity, which inherits from:
    - MetrologicalSymbol, MathematicalSymbol, Constant, Metrological, Symbol

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_442bd91e_a724_4e9f_89c1_18423016fb75'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MetricPrefix'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MetricPrefix(
    
    class_iri='https://w3id.org/emmo#EMMO_442bd91e_a724_4e9f_89c1_18423016fb75',
    
    class_name='MetricPrefix',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_442bd91e_a724_4e9f_89c1_18423016fb75',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'MetricPrefix',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    