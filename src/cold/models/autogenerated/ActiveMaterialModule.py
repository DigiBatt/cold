
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalConstituentModule import ElectrochemicalConstituent



from .ElectrochemicalMaterialModule import ElectrochemicalMaterial







class ActiveMaterial(ElectrochemicalConstituent, ElectrochemicalMaterial):
    """
    Class representing the `ActiveMaterial` entity, which inherits from:
    - ElectrochemicalConstituent, ElectrochemicalMaterial

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79d1b273_58cd_4be6_a250_434817f7c261'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ActiveMaterial'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ActiveMaterial(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79d1b273_58cd_4be6_a250_434817f7c261',
    
    class_name='ActiveMaterial',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_79d1b273_58cd_4be6_a250_434817f7c261',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ActiveMaterial',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    

    
    

    

    