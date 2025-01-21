
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .ElectricCurrentDensityUnitModule import ElectricCurrentDensityUnit



from .SINonCoherentUnitModule import SINonCoherentUnit



from .MilliPrefixedUnitModule import MilliPrefixedUnit








class MilliAmperePerSquareCentiMetre(ElectricCurrentDensityUnit, SINonCoherentUnit, MilliPrefixedUnit):
    """
    Class representing the `MilliAmperePerSquareCentiMetre` entity, which inherits from:
    - ElectricCurrentDensityUnit, SINonCoherentUnit, MilliPrefixedUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#MilliAmperePerSquareCentiMetre'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'MilliAmperePerSquareCentiMetre'`
        - **Alias**: `class_name`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = MilliAmperePerSquareCentiMetre(
    
    class_iri='https://w3id.org/emmo#MilliAmperePerSquareCentiMetre',
    
    class_name='MilliAmperePerSquareCentiMetre',
    
    hasSIConversionMultiplier="example_value",
    
    elucidation="example_value",
    
    hasSIConversionOffset="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#MilliAmperePerSquareCentiMetre',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'MilliAmperePerSquareCentiMetre',
        
        alias="class_name"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    


    
    

    

    