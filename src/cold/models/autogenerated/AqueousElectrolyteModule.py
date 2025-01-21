
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AqueousSolutionModule import AqueousSolution



from .ElectrolyteSolutionModule import ElectrolyteSolution







class AqueousElectrolyte(AqueousSolution, ElectrolyteSolution):
    """
    Class representing the `AqueousElectrolyte` entity, which inherits from:
    - AqueousSolution, ElectrolyteSolution

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b812e9d0_7c58_4455_b3e7_6847f10c8e8a'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AqueousElectrolyte'`
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
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AqueousElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b812e9d0_7c58_4455_b3e7_6847f10c8e8a',
    
    class_name='AqueousElectrolyte',
    
    wikidataReference="example_value",
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b812e9d0_7c58_4455_b3e7_6847f10c8e8a',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AqueousElectrolyte',
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
    

    
    

    

    