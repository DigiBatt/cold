
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalConstituentModule import ElectrochemicalConstituent







class EdgeInsulator(ElectrochemicalConstituent):
    """
    Class representing the `EdgeInsulator` entity, which inherits from:
    - ElectrochemicalConstituent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bbc77932_643b_4603_a4e8_970ef06a76ad'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EdgeInsulator'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EdgeInsulator(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bbc77932_643b_4603_a4e8_970ef06a76ad',
    
    class_name='EdgeInsulator',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bbc77932_643b_4603_a4e8_970ef06a76ad',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EdgeInsulator',
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
    

    
    

    

    