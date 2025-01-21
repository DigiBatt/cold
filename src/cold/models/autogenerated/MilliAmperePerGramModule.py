
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SICoherentDerivedUnitModule import SICoherentDerivedUnit



from .ElectricCurrentPerMassUnitModule import ElectricCurrentPerMassUnit








class MilliAmperePerGram(SICoherentDerivedUnit, ElectricCurrentPerMassUnit):
    """
    Class representing the `MilliAmperePerGram` entity, which inherits from:
    - SICoherentDerivedUnit, ElectricCurrentPerMassUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MilliAmperePerGram'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MilliAmperePerGram'`
        - **Alias**: `class_name`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MilliAmperePerGram(
    
    class_iri='https://w3id.org/emmo#MilliAmperePerGram',
    
    class_name='MilliAmperePerGram',
    
    hasSIConversionOffset="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MilliAmperePerGram',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MilliAmperePerGram',
        
        alias="class_name"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    


    
    

    

    