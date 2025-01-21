
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChargeNumberModule import ChargeNumber







class OxidationNumber(ChargeNumber):
    """
    Class representing the `OxidationNumber` entity, which inherits from:
    - ChargeNumber

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_26922e28_b266_46c1_b93e_4940633ba5e4'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OxidationNumber'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OxidationNumber(
    
    class_iri='https://w3id.org/emmo#EMMO_26922e28_b266_46c1_b93e_4940633ba5e4',
    
    class_name='OxidationNumber',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_26922e28_b266_46c1_b93e_4940633ba5e4',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OxidationNumber',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    dbpediaReference: Optional[str] = Field(
        None,
        alias="dbpediaReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    