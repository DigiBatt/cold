
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SIDimensionalUnitModule import SIDimensionalUnit








class PerQuarticLengthUnit(SIDimensionalUnit):
    """
    Class representing the `PerQuarticLengthUnit` entity, which inherits from:
    - SIDimensionalUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3c38a8b4_ed07_4185_8d9b_b57b9130c537'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PerQuarticLengthUnit'`
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
    obj = PerQuarticLengthUnit(
    
    class_iri='https://w3id.org/emmo#EMMO_3c38a8b4_ed07_4185_8d9b_b57b9130c537',
    
    class_name='PerQuarticLengthUnit',
    
    elucidation="example_value",
    
    hasDimensionString="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#EMMO_3c38a8b4_ed07_4185_8d9b_b57b9130c537',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'PerQuarticLengthUnit',
        
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
    


    
    

    

    