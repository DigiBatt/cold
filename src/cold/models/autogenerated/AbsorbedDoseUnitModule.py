
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit







class AbsorbedDoseUnit(SIDimensionalUnit):
    """
    Class representing the `AbsorbedDoseUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_847f1d9f_205e_46c1_8cb6_a9e479421f88'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AbsorbedDoseUnit'`
        - **Alias**: `class_name`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AbsorbedDoseUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_847f1d9f_205e_46c1_8cb6_a9e479421f88',
    
    class_name='AbsorbedDoseUnit',
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_847f1d9f_205e_46c1_8cb6_a9e479421f88',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AbsorbedDoseUnit',
        alias="class_name"
    )
    
    hasDimensionString: Optional[str] = Field(
        None,
        alias="hasDimensionString"
    )
    

    
    

    

    