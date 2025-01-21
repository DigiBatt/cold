
from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, List, Union



from .SINonCoherentUnitModule import SINonCoherentUnit



from .NonPrefixedUnitModule import NonPrefixedUnit



from .LengthUnitModule import LengthUnit








class Ångström(SINonCoherentUnit, NonPrefixedUnit, LengthUnit):
    """
    Class representing the `Ångström` entity, which inherits from:
    - SINonCoherentUnit, NonPrefixedUnit, LengthUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Angstrom'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Ångström'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `uneceCommonCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `uneceCommonCode`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Ångström(
    
    class_iri='https://w3id.org/emmo#Angstrom',
    
    class_name='Ångström',
    
    definition="example_value",
    
    hasSymbolValue="example_value",
    
    elucidation="example_value",
    
    uneceCommonCode="example_value",
    
    qudtReference="example_value",
    
    wikipediaReference="example_value",
    
    iupacReference="example_value",
    
    dbpediaReference="example_value",
    
    hasSIConversionOffset="example_value",
    
    ucumCode="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        
            'https://w3id.org/emmo#Angstrom',
        
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        
            'Ångström',
        
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        
            None,
        
        alias="definition"
    )
    
    hasSymbolValue: Optional[str] = Field(
        
            None,
        
        alias="hasSymbolValue"
    )
    
    elucidation: Optional[str] = Field(
        
            None,
        
        alias="elucidation"
    )
    
    uneceCommonCode: Optional[str] = Field(
        
            None,
        
        alias="uneceCommonCode"
    )
    
    qudtReference: Optional[str] = Field(
        
            None,
        
        alias="qudtReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        
            None,
        
        alias="wikipediaReference"
    )
    
    iupacReference: Optional[str] = Field(
        
            None,
        
        alias="iupacReference"
    )
    
    dbpediaReference: Optional[str] = Field(
        
            None,
        
        alias="dbpediaReference"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionOffset"
    )
    
    ucumCode: Optional[str] = Field(
        
            None,
        
        alias="ucumCode"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        
            None,
        
        alias="hasSIConversionMultiplier"
    )
    


    
    

    

    