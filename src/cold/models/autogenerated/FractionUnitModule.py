
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DimensionlessUnitModule import DimensionlessUnit







class FractionUnit(DimensionlessUnit):
    """
    Class representing the `FractionUnit` entity, which inherits from:
    - DimensionlessUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_c2f5ee66_579c_44c6_a2e9_fa2eaa9fa4da'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'FractionUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = FractionUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_c2f5ee66_579c_44c6_a2e9_fa2eaa9fa4da',
    
    class_name='FractionUnit',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_c2f5ee66_579c_44c6_a2e9_fa2eaa9fa4da',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'FractionUnit',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    