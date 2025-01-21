
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit








class PerLengthUnit(SIDimensionalUnit):
    """
    Class representing the `PerLengthUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fee2a014_3322_48f9_91ab_d947a6e54556'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PerLengthUnit'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasDimensionString` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasDimensionString`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PerLengthUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_fee2a014_3322_48f9_91ab_d947a6e54556',
    
    class_name='PerLengthUnit',
    
    elucidation="example_value",
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#EMMO_fee2a014_3322_48f9_91ab_d947a6e54556',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'PerLengthUnit',
        
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    hasDimensionString: Optional[str] = Field(
        
            None,
        
        alias="hasDimensionString"
    )
    


    
    

    

    