
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIUnitSymbolModule import SIUnitSymbol



from .SIDimensionalUnitModule import SIDimensionalUnit



from .BaseUnitModule import BaseUnit







class SIBaseUnit(SIUnitSymbol, SIDimensionalUnit, BaseUnit):
    """
    Class representing the `SIBaseUnit` entity, which inherits from:
    - SIUnitSymbol, SIDimensionalUnit, BaseUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3a185e6c_9e19_4776_b583_19c978156aa0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SIBaseUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SIBaseUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_3a185e6c_9e19_4776_b583_19c978156aa0',
    
    class_name='SIBaseUnit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3a185e6c_9e19_4776_b583_19c978156aa0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SIBaseUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    