
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SpecialUnitModule import SpecialUnit



from .MassUnitModule import MassUnit







class Tonne(SpecialUnit, MassUnit):
    """
    Class representing the `Tonne` entity, which inherits from:
    - SpecialUnit, MassUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Tonne'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Tonne'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `uneceCommonCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `uneceCommonCode`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `hasSIConversionOffset` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionOffset`
    
    - `hasSIConversionMultiplier` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSIConversionMultiplier`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Tonne(
    
    class_iri='https://w3id.org/emmo#Tonne',
    
    class_name='Tonne',
    
    iupacReference="example_value",
    
    hasSymbolValue="example_value",
    
    definition="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    uneceCommonCode="example_value",
    
    elucidation="example_value",
    
    hasSIConversionOffset="example_value",
    
    hasSIConversionMultiplier="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#Tonne',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Tonne',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    hasSymbolValue: Optional[str] = Field(
        None,
        alias="hasSymbolValue"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    ucumCode: Optional[str] = Field(
        None,
        alias="ucumCode"
    )
    
    uneceCommonCode: Optional[str] = Field(
        None,
        alias="uneceCommonCode"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    hasSIConversionOffset: Optional[str] = Field(
        None,
        alias="hasSIConversionOffset"
    )
    
    hasSIConversionMultiplier: Optional[str] = Field(
        None,
        alias="hasSIConversionMultiplier"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    