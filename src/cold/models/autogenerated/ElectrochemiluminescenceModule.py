
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalPhenomenonModule import ElectrochemicalPhenomenon







class Electrochemiluminescence(ElectrochemicalPhenomenon):
    """
    Class representing the `Electrochemiluminescence` entity, which inherits from:
    - ElectrochemicalPhenomenon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_96309fa9_e157_48fe_9fda_41003860a3c0'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Electrochemiluminescence'`
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
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Electrochemiluminescence(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_96309fa9_e157_48fe_9fda_41003860a3c0',
    
    class_name='Electrochemiluminescence',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_96309fa9_e157_48fe_9fda_41003860a3c0',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Electrochemiluminescence',
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
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    