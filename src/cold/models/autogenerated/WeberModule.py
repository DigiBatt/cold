
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MagneticFluxUnitModule import MagneticFluxUnit



from .SISpecialUnitModule import SISpecialUnit







class Weber(MagneticFluxUnit, SISpecialUnit):
    """
    Class representing the `Weber` entity, which inherits from:
    - MagneticFluxUnit, SISpecialUnit

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#Weber'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Weber'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `hasSymbolValue` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `hasSymbolValue`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ucumCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ucumCode`
    
    - `uneceCommonCode` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `uneceCommonCode`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Weber(
    
    class_iri='https://w3id.org/emmo#Weber',
    
    class_name='Weber',
    
    iupacReference="example_value",
    
    hasSymbolValue="example_value",
    
    qudtReference="example_value",
    
    ucumCode="example_value",
    
    uneceCommonCode="example_value",
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#Weber',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Weber',
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
    
    dbpediaReference: Optional[str] = Field(
        None,
        alias="dbpediaReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    