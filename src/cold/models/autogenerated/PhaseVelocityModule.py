
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .VelocityModule import Velocity







class PhaseVelocity(Velocity):
    """
    Class representing the `PhaseVelocity` entity, which inherits from:
    - Velocity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2b69b940_a4ab_40dc_b565_8daab23e4df2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PhaseVelocity'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PhaseVelocity(
    
    class_iri='https://w3id.org/emmo#EMMO_2b69b940_a4ab_40dc_b565_8daab23e4df2',
    
    class_name='PhaseVelocity',
    
    wikidataReference="example_value",
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2b69b940_a4ab_40dc_b565_8daab23e4df2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PhaseVelocity',
        alias="class_name"
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
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    