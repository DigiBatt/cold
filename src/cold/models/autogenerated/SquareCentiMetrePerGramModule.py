
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .AreaPerMassUnitModule import AreaPerMassUnit



from .SINonCoherentDerivedUnitModule import SINonCoherentDerivedUnit








class SquareCentiMetrePerGram(AreaPerMassUnit, SINonCoherentDerivedUnit):
    """
    Class representing the `SquareCentiMetrePerGram` entity, which inherits from:
    - AreaPerMassUnit, SINonCoherentDerivedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#SquareCentMetrePerGram'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SquareCentiMetrePerGram'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SquareCentiMetrePerGram(
    
    class_iri='https://w3id.org/emmo#SquareCentMetrePerGram',
    
    class_name='SquareCentiMetrePerGram',
    
    hasSIConversionMultiplier="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#SquareCentMetrePerGram',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'SquareCentiMetrePerGram',
        
        alias="class_name"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    


    
    

    

    