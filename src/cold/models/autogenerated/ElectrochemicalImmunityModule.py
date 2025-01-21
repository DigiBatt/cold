
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPhenomenonModule import ElectrochemicalPhenomenon







class ElectrochemicalImmunity(ElectrochemicalPhenomenon):
    """
    Class representing the `ElectrochemicalImmunity` entity, which inherits from:
    - ElectrochemicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4bc38e99_1978_4143_a766_fbb57f2cf46e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalImmunity'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalImmunity(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4bc38e99_1978_4143_a766_fbb57f2cf46e',
    
    class_name='ElectrochemicalImmunity',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_4bc38e99_1978_4143_a766_fbb57f2cf46e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalImmunity',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    